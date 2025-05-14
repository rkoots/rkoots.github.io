import os
import re
import feedparser
from datetime import datetime
import google.generativeai as genai
# Configure Gemini
api_key=os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key is not set in the environment variables")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


today = datetime.today().strftime("%Y-%m-%d")

RSS_FEEDS = [
    "https://feeds.feedburner.com/TechCrunch/",
    "https://www.theverge.com/rss/index.xml",
    "https://www.wired.com/feed/rss",
    "https://www.cnet.com/rss/all/",
    "https://www.zdnet.com/news/rss.xml",
    "https://arstechnica.com/feed/",
    "https://www.engadget.com/rss.xml"
]

used_topics_file = "used_topics.json"
if os.path.exists(used_topics_file):
    with open(used_topics_file, "r") as f:
        used_topics = json.load(f)
else:
    used_topics = []

random.shuffle(RSS_FEEDS)
topic = None



for url in RSS_FEEDS:
    feed = feedparser.parse(url)
    entries = feed.entries
    random.shuffle(entries)

    for entry in entries:
        title = entry.title.strip()
        link = entry.link.strip()
        if title not in used_topics:
            topic = {"title": title, "link": link}
            used_topics.append(title)
            break
    if topic:
        break

if not topic:
    raise Exception("No new topics found in any feed.")

prompt = f"""
You are a tech journalist writing for a Jekyll blog. Write a trending blog post in Markdown format using the following front matter and tech topic from today ({today}).

Topic: {topic['title']}
Source: {topic['link']}

---
layout: default
title: "{topic['title']}"
date: {today}
categories: blog
author: "rkoots Bot"
tags: [technology, innovation, AI]
keywords: [tech, {topic['title']}, {today}]
---

## {topic['title']}

Write an informative and engaging article about the topic above. Include relevant technical details, implications, or industry impact. End with a link to the original source for reference.
"""

# Generate response
response = model.generate_content(prompt)
print(response)
markdown_output = response.text.strip()

# Extract title from front matter
title_match = re.search(r'title:\s*["\']?(.+?)["\']?\s*$', markdown_output, re.MULTILINE)
if not title_match:
    raise ValueError("Could not extract title from the markdown output.")

title = title_match.group(1)

# Create slug from title
slug = re.sub(r'[^\w\s-]', '', title).strip().lower()
slug = re.sub(r'[\s_]+', '-', slug)

# Create filename using today's date
filename = f"_posts/{today}-{slug}.md"

# Save the output to a Markdown file
os.makedirs("_posts", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown_output)

print(f"✅ Gemini post saved as {filename}")
