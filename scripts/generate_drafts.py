"""Fetch recent commits from all repos, group by theme, generate blog drafts via Gemini."""
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GH_TOKEN = os.environ.get("GH_TOKEN", "")
OWNER = "Seithx"
MARKER_FILE = ".last_draft_gen"
DRAFTS_DIR = "drafts"

# Repos to skip (blog itself, profile, forks, personal-only)
SKIP_REPOS = {
    "Seithx.github.io",
    "Seithx",
    "ojt-presentation-icons",
    "smarthebrewrtl-extension-landing",
    "smart-hebrew-rtl",
    "termux-android-media-tools",
    "dev-environment-bootstrap",
}

# Sensitive repos: strip specifics, keep generic
SENSITIVE_REPOS = {
    "NotebookLM-Chatwrapper": "a web app API wrapper using browser automation",
    "waha-monitor": "a messaging monitor with AI-powered daily digests",
    "ExtractorArticlesFromIsraeliNewsSites": "a Hebrew news article extraction service",
    "Invoice-System": "an AI-powered invoice processing system for ERP integration",
    "joni-extension-reverse-engineering": None,  # skip entirely
    "RHGROUPWHATSAPPAUTOMATION": None,  # skip
}

# Map repo names to friendlier public descriptions
REPO_DESCRIPTIONS = {
    "NotebookLM-Chatwrapper": "Browser Automation API Wrapper",
    "waha-monitor": "Personal Information Hub",
    "Invoice-System": "AI Invoice Processing",
    "ExtractorArticlesFromIsraeliNewsSites": "Hebrew News Extractor",
    "floorsight": "FloorSight Video Analysis",
    "EnhanchedSynagouge": "Synagogue Display System",
    "ups-shipping-calculator": "Shipping Cost Calculator",
    "mikyab-rag-pipeline": "RAG Knowledge Base Pipeline",
    "rationalbelief-rag-pipeline": "RAG Knowledge Base Pipeline",
    "recorder-cli": "Google Recorder CLI",
    "rhgroup-cheezos-video-compressor": "Video Compressor (Electron)",
    "rhgroup-electron-audio-converter": "Audio Converter (Electron)",
    "Relixor": "Relixor Mobile Browser",
    "rhgroup-scan-convert": "Scan Converter",
    "ups-tracking-dashboard": "Shipping Tracking Dashboard",
    "MONDAY-API-DASHBOARD": "Monday.com Dashboard",
    "PromptEvolutionist": "Prompt Evolution Tool",
}


def gh_api(endpoint):
    """Call GitHub API with PAT auth."""
    url = f"https://api.github.com/{endpoint}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {GH_TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"  [WARNING] API error {e.code} for {endpoint}")
        return []


def gemini_call(prompt, system_prompt):
    """Call Gemini 2.5 Flash API."""
    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    )
    body = json.dumps({
        "systemInstruction": {
            "role": "system",
            "parts": [{"text": system_prompt}],
        },
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.1, "thinkingConfig": {"thinkBudget": -1}},
    }).encode()

    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/json")

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode())
            err = data.get("error", {}).get("message")
            if err:
                print(f"  [WARNING] Gemini error: {err}")
                return None
            parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
            text = "\n".join(p.get("text", "") for p in parts)
            return text if text and text != "null" else None
        except Exception as e:
            print(f"  [WARNING] Gemini attempt {attempt+1} failed: {e}")
            import time
            time.sleep(5 * (attempt + 1))
    return None


def get_since_date():
    """Get the date to fetch commits from."""
    if os.path.exists(MARKER_FILE):
        with open(MARKER_FILE) as f:
            date_str = f.read().strip()
        try:
            return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except ValueError:
            pass
    # Default: 2 weeks ago
    return datetime.now(timezone.utc) - timedelta(days=14)


def save_marker():
    """Save current timestamp as marker."""
    with open(MARKER_FILE, "w") as f:
        f.write(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))


def fetch_repos():
    """Get all repos for the user."""
    repos = []
    page = 1
    while True:
        batch = gh_api(f"users/{OWNER}/repos?per_page=100&page={page}&type=owner")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def fetch_commits_all_branches(repo_name, since_iso):
    """Fetch commits from ALL branches since a date."""
    branches = gh_api(f"repos/{OWNER}/{repo_name}/branches?per_page=100")
    if not branches:
        return []

    seen_shas = set()
    all_commits = []

    for branch in branches:
        branch_name = branch["name"]
        commits = gh_api(
            f"repos/{OWNER}/{repo_name}/commits"
            f"?sha={branch_name}&since={since_iso}&per_page=50"
        )
        for c in commits:
            sha = c.get("sha", "")
            if sha not in seen_shas:
                seen_shas.add(sha)
                msg = c.get("commit", {}).get("message", "").split("\n")[0]
                date = c.get("commit", {}).get("author", {}).get("date", "")
                all_commits.append({
                    "date": date,
                    "message": msg,
                    "branch": branch_name,
                })

    all_commits.sort(key=lambda x: x["date"])
    return all_commits


def sanitize_commits(repo_name, commits):
    """Remove sensitive details from commit messages."""
    desc = SENSITIVE_REPOS.get(repo_name)
    if desc is None and repo_name in SENSITIVE_REPOS:
        return []  # skip entirely

    sanitized = []
    for c in commits:
        msg = c["message"]
        # Strip common sensitive patterns
        for pattern in ["RH Group", "rhgroup", "mikyab", "rationalbelief",
                        "WAHA", "waha", "NotebookLM", "notebooklm",
                        "Priority ERP", "priority"]:
            msg = msg.replace(pattern, "***")
        sanitized.append({**c, "message": msg})
    return sanitized


def group_repos_into_drafts(repo_commits):
    """Group repos into draft topics. Returns list of (title, commit_text) pairs."""
    # Combine small repos, keep large ones separate
    MIN_COMMITS = 3
    large = {}
    small_bucket = {}

    for repo_name, commits in repo_commits.items():
        if len(commits) >= MIN_COMMITS:
            large[repo_name] = commits
        else:
            small_bucket[repo_name] = commits

    groups = []

    # Each large repo gets its own draft
    for repo_name, commits in large.items():
        friendly = REPO_DESCRIPTIONS.get(repo_name, repo_name)
        commit_lines = [f"- [{c['date'][:10]}] {c['message']}" for c in commits]
        groups.append((friendly, repo_name, "\n".join(commit_lines)))

    # Small repos get bundled into one "roundup" draft
    if small_bucket:
        lines = []
        for repo_name, commits in small_bucket.items():
            friendly = REPO_DESCRIPTIONS.get(repo_name, repo_name)
            lines.append(f"\n{friendly}:")
            for c in commits:
                lines.append(f"- [{c['date'][:10]}] {c['message']}")
        groups.append(("Side Projects Roundup", "misc", "\n".join(lines)))

    return groups


SYSTEM_PROMPT = """\
You are generating raw dev notes for a developer's personal blog. The blog is a \
learning journal -- personal, diary-style, honest about struggles and growth.

Given a list of git commits from a project, write raw notes (NOT a finished blog post) \
that capture:
1. What the project is and why it exists (2-3 sentences of background)
2. What was done in this period (key features, fixes, milestones)
3. What was hard or surprising (struggles, bugs, unexpected lessons)
4. A personal reflection (how it felt, what was learned, how it connects to growth)
5. What's next (1 line)

RULES:
- Write 300-600 words of raw, informal notes
- Use the developer's voice: first person, honest, sometimes self-deprecating
- Do NOT mention specific company names, client names, or repository names
- Do NOT reveal auth bypass techniques, scraping methods, or security workarounds
- Do NOT format as a finished blog post -- this is raw input for another LLM
- Start with "Raw dev notes --" and a rough title idea
- Include enough detail for a blog-post editor to work with
- Keep it grounded in the actual commits -- don't invent features that aren't there
"""


def generate_draft(title, repo_key, commits_text):
    """Call Gemini to generate a draft from commits."""
    prompt = (
        f"Project: {title}\n\n"
        f"Recent commits:\n{commits_text}\n\n"
        f"Generate raw dev notes for a blog post about this work."
    )
    return gemini_call(prompt, SYSTEM_PROMPT)


def make_slug(title):
    """Convert title to a filename-safe slug."""
    slug = title.lower()
    for ch in " /\\:*?\"<>|'(),.!":
        slug = slug.replace(ch, "-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")[:60]


def main():
    if not GEMINI_API_KEY:
        print("[ERROR] GEMINI_API_KEY not set")
        sys.exit(1)
    if not GH_TOKEN:
        print("[ERROR] GH_TOKEN not set")
        sys.exit(1)

    since = get_since_date()
    since_iso = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"Fetching commits since {since_iso}")

    # Fetch all repos
    repos = fetch_repos()
    print(f"Found {len(repos)} repos")

    # Fetch commits for each active repo
    repo_commits = {}
    for repo in repos:
        name = repo["name"]
        if name in SKIP_REPOS:
            continue
        if repo.get("fork") and name not in REPO_DESCRIPTIONS:
            continue

        commits = fetch_commits_all_branches(name, since_iso)
        if not commits:
            continue

        commits = sanitize_commits(name, commits)
        if not commits:
            continue

        print(f"  {name}: {len(commits)} commits across branches")
        repo_commits[name] = commits

    if not repo_commits:
        print("No new commits to process.")
        save_marker()
        return

    # Group into draft topics
    groups = group_repos_into_drafts(repo_commits)
    print(f"\nGenerating {len(groups)} drafts...")

    os.makedirs(DRAFTS_DIR, exist_ok=True)
    generated = 0

    for title, repo_key, commits_text in groups:
        slug = make_slug(repo_key if repo_key != "misc" else "side-projects-roundup")
        draft_path = os.path.join(DRAFTS_DIR, slug)

        # Skip if draft already exists
        if os.path.exists(draft_path):
            print(f"  [SKIP] {draft_path} already exists")
            continue

        print(f"  Generating: {title} -> {draft_path}")
        text = generate_draft(title, repo_key, commits_text)
        if text:
            with open(draft_path, "w", encoding="utf-8") as f:
                f.write(text.strip() + "\n")
            generated += 1
            print(f"  [OK] {draft_path}")
        else:
            print(f"  [ERROR] Failed to generate draft for {title}")

    save_marker()
    print(f"\n[OK] Generated {generated} new drafts, marker updated")


if __name__ == "__main__":
    main()
