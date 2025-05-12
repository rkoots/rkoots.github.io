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

prompt = f"""
You are a tech analyst writing for a Jekyll gadget of the day post. Based write a short brief of tool in Markdown format with this exact front matter structure from the latest tech tools of today:

---
layout: default
title: "<best sutaiable>"
date: {{today}}
categories: tool
author: "rkoots research Bot"
tags: [<relavent tag list>]
keywords: [<relavent keyword list>]
---

## <best attractive sutaiable title>

Write about tools with about one tool of the day with link to the tool trending from technology, IT, AI, ML or gadgets (example : home.by.me, make.com, notion.com). Be concise, informative, and objective. In random design content format supported by MD file with details to links, how it works, documentation links, and reference also that we have online. 

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
