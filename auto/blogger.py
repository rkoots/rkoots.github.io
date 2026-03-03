import datetime
import json
import os
import re
from pathlib import Path
from typing import Tuple, List
import requests

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
POSTS_DIR = ROOT_DIR / "blog" / "_posts"
HISTORY_FILE = BASE_DIR / "blog_history.json"

# Gemini API configuration
GEMINI_API_KEY = os.getenv("KEY")
FORCE_RUN = os.getenv("FORCE_RUN", "false").lower() == "true"


def load_blog_history() -> List[str]:
    """Load previously used topics to avoid duplicates"""
    if not HISTORY_FILE.exists():
        return []
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('used_topics', [])
    except (json.JSONDecodeError, KeyError):
        return []


def save_topic_to_history(topic: str):
    """Save topic to history to prevent duplicates"""
    history = load_blog_history()
    if topic not in history:
        history.append(topic)
        # Keep only last 50 topics
        history = history[-50:]
        
        data = {'used_topics': history}
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def get_trending_ai_topics() -> List[str]:
    """Generate trending AI topics using Gemini"""
    if not GEMINI_API_KEY:
        print("Warning: GEMINI_API_KEY not set, using fallback topics")
        return [
            "AI Code Assistants in Software Development",
            "Machine Learning in Production Systems",
            "Large Language Models for Business Applications",
            "AI Ethics and Responsible AI Development",
            "Automated Testing with AI Tools"
        ]
    
    prompt = """Generate 5 trending AI/ML topics that are currently popular in the tech industry. 
Focus on new tools, techniques, or methodologies. Return only a JSON array of topic strings.
Topics should be specific and interesting for technical audiences.
Example: ["AI-powered debugging tools", "Retrieval Augmented Generation best practices", "MLOps automation"]
"""
    
    try:
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}",
            headers={'Content-Type': 'application/json'},
            json={
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result['candidates'][0]['content']['parts'][0]['text']
            # Extract JSON array from response
            import re
            json_match = re.search(r'\[.*?\]', content, re.DOTALL)
            if json_match:
                topics = json.loads(json_match.group())
                return topics[:5]  # Ensure max 5 topics
        
        print(f"Gemini API error: {response.status_code}")
        return get_fallback_topics()
        
    except Exception as e:
        print(f"Error fetching topics from Gemini: {e}")
        return get_fallback_topics()


def get_fallback_topics() -> List[str]:
    """Fallback topics when Gemini fails"""
    return [
        "AI Code Generation Tools Comparison",
        "Building Production-Ready LLM Applications",
        "AI Testing Strategies for Modern Development",
        "Machine Learning Operations Best Practices",
        "AI-Powered DevOps Automation"
    ]


def select_new_topic() -> str:
    """Select a topic that hasn't been used before"""
    used_topics = load_blog_history()
    trending_topics = get_trending_ai_topics()
    
    # Find first unused topic
    for topic in trending_topics:
        if topic not in used_topics:
            save_topic_to_history(topic)
            return topic
    
    # If all trending topics are used, use a fallback with date
    topic = f"AI Insights - {datetime.datetime.now().strftime('%Y-%m-%d')}"
    save_topic_to_history(topic)
    return topic


def generate_blog_content_with_gemini(topic: str) -> str:
    """Generate blog content using Gemini API"""
    if not GEMINI_API_KEY:
        return generate_fallback_content(topic)
    
    prompt = f"""Write a comprehensive blog post about: "{topic}"

Requirements:
- Target audience: Software engineers and technical leaders
- Length: 800-1200 words
- Include practical examples and code snippets where relevant
- Structure: Introduction, Main Content (2-3 sections), Conclusion
- Tone: Professional but engaging
- Include actionable insights
- Format in markdown

Focus on current trends, best practices, and real-world applications.
"""
    
    try:
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}",
            headers={'Content-Type': 'application/json'},
            json={
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result['candidates'][0]['content']['parts'][0]['text']
            return content
        
        print(f"Gemini content generation error: {response.status_code}")
        return generate_fallback_content(topic)
        
    except Exception as e:
        print(f"Error generating content with Gemini: {e}")
        return generate_fallback_content(topic)


def generate_fallback_content(topic: str) -> str:
    """Generate fallback content when Gemini fails"""
    return f"""# {topic}

## Introduction

In the rapidly evolving landscape of artificial intelligence and machine learning, staying current with emerging tools and techniques is crucial for development teams. This post explores key insights and practical approaches for implementing {topic.lower()} in modern software development.

## Key Considerations

### Technical Implementation

When implementing {topic.lower()}, consider the following aspects:

- **Performance**: Ensure the solution meets your latency requirements
- **Scalability**: Design for growth and increased usage
- **Maintainability**: Build systems that are easy to update and debug
- **Security**: Implement proper safeguards for AI-powered features

### Best Practices

1. Start with small, focused experiments
2. Measure impact with clear metrics
3. Iterate based on user feedback
4. Maintain human oversight for critical decisions

## Practical Applications

### Use Case 1: Development Workflow

Integrating {topic.lower()} into daily development processes can significantly improve productivity and code quality.

### Use Case 2: Production Systems

For production environments, ensure robust error handling and monitoring for {topic.lower()} implementations.

## Conclusion

{topic} represents an important trend in modern software development. By approaching implementation thoughtfully and focusing on practical value, teams can successfully leverage these technologies to build better products.

*Published on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*
"""


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\s-]", "", value.lower()).strip()
    return re.sub(r"[\s_-]+", "-", slug)


def build_title(topic: str, now_utc: datetime.datetime) -> str:
    return f"{topic} - {now_utc.strftime('%d %b %Y')}"


def build_markdown_post(topic: str, content: str, now_utc: datetime.datetime) -> str:
    date_str = now_utc.strftime("%Y-%m-%d")
    pub_str = now_utc.strftime("%Y-%m-%d %H:%M UTC")
    
    # Extract first paragraph for description
    lines = content.split('\n')
    first_paragraph = ""
    for line in lines:
        if line.strip() and not line.startswith('#'):
            first_paragraph = line.strip()
            break
    
    return f"""---
layout: default
title: "{topic} - {now_utc.strftime('%d %b %Y')}"
date: {date_str}
author: Rajkumar V.
categories: [AI, Technology, Engineering]
tags: [AI, Machine Learning, Software Development, Technology Trends]
description: {first_paragraph[:200]}...
---

{content}"""


def is_publish_day(now_utc: datetime.datetime) -> bool:
    # Wednesday=2, Friday=4
    return now_utc.weekday() in {2, 4}


def generate_post_file(now_utc: datetime.datetime) -> Tuple[Path, str]:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Select a new trending topic
    topic = select_new_topic()
    print(f"Selected topic: {topic}")
    
    # Generate content using Gemini
    content = generate_blog_content_with_gemini(topic)
    print(f"Generated content length: {len(content)} characters")
    
    # Build title and markdown
    title = build_title(topic, now_utc)
    slug = slugify(title)
    file_name = f"{now_utc.strftime('%Y-%m-%d')}-{slug}.md"
    post_path = POSTS_DIR / file_name
    
    # Create and save the post
    post_markdown = build_markdown_post(topic, content, now_utc)
    post_path.write_text(post_markdown, encoding="utf-8")
    
    return post_path, title


def main():
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    
    print(f"🤖 AI Blog Generator started at {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")

    if not FORCE_RUN and not is_publish_day(now_utc):
        print("ℹ️ Not a Wednesday/Friday run. Skipping generation.")
        return
    
    print("🚀 Starting blog post generation...")
    
    try:
        post_path, title = generate_post_file(now_utc)
        print(f"✅ Generated post file: {post_path}")
        print(f"📝 Post title: {title}")
        print(f"📁 File size: {post_path.stat().st_size} bytes")
        
        # Verify file was created successfully
        if post_path.exists() and post_path.stat().st_size > 1000:
            print("🎉 Blog post generated successfully!")
        else:
            print("❌ Warning: Generated file may be empty or too small")
            
    except Exception as e:
        print(f"❌ Error generating blog post: {e}")
        raise


if __name__ == "__main__":
    main()
