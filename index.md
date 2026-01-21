---
layout: default
title: Seithx’s Dev Notes
Personal Blog for Asaf Lecht's development process :) 
---

# Seithx’s Dev Notes
A light, human log of learning. New posts twice a week.

<ul>
{% for post in site.posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> — {{ post.date | date: "%b %d, %Y" }}</li>
{% endfor %}
</ul>
