# Asaf’s Dev Notes
A light, human log of learning. New posts twice a week.

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%b %d, %Y" }}
{% endfor %}
