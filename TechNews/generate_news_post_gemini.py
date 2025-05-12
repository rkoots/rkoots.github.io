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

# Use the Gemini Pro model
model = genai.GenerativeModel("gemini-1.5-flash")

# Fetch the latest tech article from TechCrunch RSS
FEED_URL = "https://techcrunch.com/feed/"
feed = feedparser.parse(FEED_URL)
latest_entry = feed.entries[0]
headline = latest_entry.title
url = latest_entry.link

# Date and slug formatting
today = datetime.today().strftime('%Y-%m-%d')
slug = re.sub(r'[^\w\s-]', '', headline.lower())
slug = re.sub(r'\s+', '-', slug)
filename = f"_posts/{today}-{slug}.md"
print(filename)
# Prompt for Gemini
prompt = f"""
You are a tech journalist writing for a Jekyll blog. Based on the following headline and link, write a clear and trending article in Markdown format with this exact front matter structure:

---
layout: default
title: "{headline}"
date: {today}
categories: tech-news
author: "GPT News Bot"
tags: [Technology, AI, News]
keywords: [Tech News, AI, Startups, Innovation]
---

## {headline}

Write a decent big tech news article summarizing or expanding on this topic.
Be concise, informative, and objective.

URL: {url}
"""

# Generate response
response = model.generate_content(prompt)
print(response)
markdown_output = response.text.strip()

# Save the output to a Markdown file
os.makedirs("_posts", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown_output)

print(f"✅ Gemini post saved as {filename}")
