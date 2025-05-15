import os
import re
import feedparser
from datetime import datetime
import google.generativeai as genai
import random

# --- CONFIGURATION ---

# Setup Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key is not set in the environment variables")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# RSS feeds from 3 top tech sites
rss_feeds = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Wired": "https://www.wired.com/feed/rss"
}

# --- FETCH AND SELECT ARTICLE ---

# Parse all feeds and collect entries
articles = []

for source, url in rss_feeds.items():
    feed = feedparser.parse(url)
    for entry in feed.entries:
        if "summary" in entry and "link" in entry:
            articles.append({
                "source": source,
                "title": entry.title,
                "link": entry.link,
                "summary": re.sub('<[^<]+?>', '', entry.summary)  # Clean HTML tags
            })

# Ensure articles were fetched
if not articles:
    raise ValueError("No articles found from any RSS feed.")

# Pick a random article
article = random.choice(articles)

# --- BUILD PROMPT ---

today = datetime.today().strftime("%Y-%m-%d")

prompt = f"""
You are a tech journalist writing for a Jekyll blog. Based on the following tech news summary from {article['source']}, write a clear and trending news article in Markdown format with this exact front matter structure:

News Title: {article['title']}
News Summary: {article['summary']}
Source: {article['link']}

---

layout: default
title: "{article['title']}"
date: {today}
categories: news
author: "news Bot"
tags: [technology, innovation, startup, AI]
keywords: [tech, {article['title'].lower().replace(' ', '-')}, news]
---

## {article['title']}

Write a detailed news post based on this news topic. Include expanded technical details, relevance in the tech/startup/AI industry, and cite the original source ({article['link']}) at the end for reference.
"""

# --- GENERATE CONTENT ---

response = model.generate_content(prompt)

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
