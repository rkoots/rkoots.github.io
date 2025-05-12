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

prompt = f"""
You are a tech journalist writing for a Jekyll blog. Based on the following headline and link, write a clear and trending article in Markdown format with this exact front matter structure:

---
layout: default
title: <best sutaiable>
date: YYYY-MM-DD
categories: tech-news
author: "GPT News Bot"
tags: [Technology, AI, News]
keywords: [Tech News, AI, Startups, Innovation]
---

## <best attractive sutaiable title>

Write a decent big tech news article summarizing or expanding on this topic.
Be concise, informative, and objective.
<Anything latest news from technology, IT , AI etc.>
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
