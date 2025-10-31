---
layout: post
title: "The LiveView Like Button Saga"
date: 2025-10-31
source_draft: "drafts/.gitkeep"
---

I decided to tackle what I thought would be a simple feature: a "like" button. It's a classic for a reason! Building it in Phoenix LiveView was a fantastic learning experience, especially when it came to making it update in real-time for everyone, not just the person clicking the button.

Here’s a breakdown of what I learned and where I got stuck:

*   **Schema First:** The foundation was a simple Ecto `Like` schema joining my `User` and `Post` tables. The real key was adding a `unique_index` on `[:user_id, :post_id]`. This prevents a user from liking the same post multiple times at the database level—a crucial safety net.
*   **A Stateful Component:** I built a stateful `LikeComponent`. On `mount`, it determines two things: the total like count for the post, and whether the *current* user has already liked it. These two assigns (`likes_count` and `liked_by_user?`) drive the component's UI.
*   **The Initial Click:** A `phx-click` event on the button worked great for the active user. My `handle_event` function would create or delete the like record, then update the socket's assigns to re-render the button and count locally. So far, so good.
*   **The Real-Time Problem:** My component worked perfectly… for me. If another user liked the same post, my like count wouldn't update until I refreshed the page. This broke the "live" part of LiveView and was the main hurdle.
*   **PubSub to the Rescue:** The answer was `Phoenix.PubSub`. Now, after any like is created or deleted, my application broadcasts a message on a topic unique to that post (e.g., `"likes:#{post.id}"`). The `LikeComponent` subscribes to this topic when it mounts.
*   **The `handle_info` Nuance:** My component now has a `handle_info` function to catch these broadcasts. The big insight here was to *only* update the public `likes_count` from the broadcast. The `liked_by_user?` assign is personal to each user and shouldn't be changed by a global message. This prevents the UI from flickering for the person who actually clicked the button.

This feature really cemented my understanding of the LiveView process lifecycle. It's one thing to handle events for a single user, but another to broadcast state changes to many clients. The separation between user-specific state and public, broadcasted state was the big "aha!" moment. PubSub feels like a superpower once you get the hang of it.

**Next:** I want to explore adding optimistic UI updates to make the button feel even more responsive.

---
*Tags: phoenix, liveview, elixir, ecto, pubsub, real-time*
