---
layout: default
title: "Asaf Lecht - Developer Blog"
description: "Developer learning journal by Asaf Lecht (אסף לכט). AI automation, browser tooling, RAG pipelines, and Hebrew tech."
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Asaf Lecht - Dev Blog",
  "url": "https://seithx.github.io",
  "description": "Developer learning journal by Asaf Lecht",
  "author": {
    "@type": "Person",
    "name": "Asaf Lecht",
    "alternateName": "אסף לכט",
    "url": "https://github.com/Seithx",
    "jobTitle": "Full-Stack AI/Data Engineer",
    "sameAs": [
      "https://github.com/Seithx",
      "https://www.linkedin.com/in/asaflecht"
    ]
  }
}
</script>

# Asaf Lecht | אסף לכט

Full-Stack AI/Data Engineer in Israel. I build AI-powered automation and write about the process -- struggles, breakthroughs, and lessons learned.

[About](/about/) | [GitHub](https://github.com/Seithx) | [LinkedIn](https://www.linkedin.com/in/asaflecht)

---

## Posts

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})** -- {{ post.date | date: "%B %d, %Y" }}
{% endfor %}
