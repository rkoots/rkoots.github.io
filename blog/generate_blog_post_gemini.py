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
print(today)
prompt = f"""
You are a tech journalist writing for a Jekyll blog. Based write a clear and trending article in Markdown format with this exact front matter structure from the latest tech innovative topic of today:

---
layout: default
title: "<best sutaiable>"
date: {{today}} (must be todays date)
categories: blog
author: "rkoots Bot"
tags: [<Create a list>]
keywords: [<Create a list>]
---

## <best attractive sutaiable title>

Write a decent big tech topic article summarizing or expanding on this topic, more detailed technical specifications and details of today's trending topic from technology, AI, ML or gadgets with actual reference links of source for further references. Be concise, informative, and objective.
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
