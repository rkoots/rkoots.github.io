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

# Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FORCE_RUN = os.getenv("FORCE_RUN", "false").lower() == "true"

import random

TOPICS = [
    "Best AI testing tools for developers",
    "Jekyll SEO checklist for GitHub Pages",
    "Free automation tools for solo founders",
    "Claude vs ChatGPT for engineering workflows",
    "AI-powered code review tools and practices",
    "Top MLOps platforms for startup teams",
    "How to use GitHub Actions for daily automation",
    "Automating social media for tech blogs",
    "Best open-source LLMs for local development",
    "Prompt engineering techniques for software engineers",
    "Building RAG applications with LangChain",
    "Integrating AI into CI/CD pipelines",
    "Developer productivity tools powered by AI",
    "Cost optimization for cloud machine learning",
    "Serverless architecture for AI applications",
    "Vector databases comparison for RAG",
    "Fine-tuning vs RAG for enterprise use cases",
    "AI-assisted technical writing and documentation",
    "Security considerations for LLM applications",
    "Best VS Code extensions for AI development",
    "Automated testing frameworks for React applications",
    "Python web scraping with AI integration",
    "Deploying machine learning models to production",
    "Top database tools for modern web apps",
    "AI image generation APIs for developers",
    "Building chatbots with Next.js and OpenAI",
    "Best practices for API design in 2024",
    "Monitoring and observability for AI systems",
    "Tech stack choices for solo developers",
    "Automating DevOps workflows with Python",
    "Best static site generators for developer blogs",
    "Optimizing Core Web Vitals for tech blogs",
    "Data engineering tools for small teams",
    "Machine learning algorithms every developer should know",
    "Setting up local AI development environments",
    "Evaluating LLM performance and metrics",
    "AI tools for database query optimization",
    "Frontend frameworks comparison for AI apps",
    "Best practices for storing API keys and secrets",
    "Automated dependency updates and security scanning",
    "Building scalable microservices with AI capabilities",
    "Creating personalized user experiences with ML",
    "AI tools for software architecture design",
    "Using AI for log analysis and debugging",
    "Continuous deployment strategies for AI models",
    "Best practices for technical SEO",
    "Monetization strategies for tech blogs",
    "Open-source alternatives to enterprise AI tools",
    "Future trends in software engineering",
    "Writing efficient prompts for code generation",
    "Building multimodal AI applications",
    "Privacy-first machine learning techniques",
    "Automated code refactoring with AI"
]

def generate_blog_content_with_gemini(topic: str, now_utc: datetime.datetime) -> Tuple[str, str]:
    """Generate blog title and content using Gemini API"""
    current_date = now_utc.strftime("%B %d, %Y")
    
    if not GEMINI_API_KEY:
        return f"{topic} - Latest Updates", generate_fallback_content(topic)
    
    prompt = f"""Today is {current_date}. 
You are an expert technical writer and researcher. 
Please research the internet for the latest news, updates, and trends regarding exactly this topic: "{topic}".

Based on the latest information, please generate:
1. A catchy, news-driven blog post title
2. A comprehensive blog post of 1500-2500 words.

Requirements for the blog post:
- Target audience: Software engineers, developers, and technical leaders
- Word count: greater than 3000 words
- Tone: Professional, authoritative, and engaging
- Structure MUST include:
  - An engaging Introduction
  - Table of Contents
  - Main Content (multiple sections with deep dives)
  - Comparison tables (where applicable, using Markdown tables)
  - Internal linking suggestions (placeholders like `[Internal Link: Related Topic](/)`)
  - Frequently Asked Questions (FAQs) section at the end
  - Conclusion
- Include practical examples, code snippets (if relevant), and actionable insights.
- Format the entire response in Markdown.

Please format your response EXACTLY as follows:
TITLE: [Your generated title here]
CONTENT:
[Your markdown content here]
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
            text = result['candidates'][0]['content']['parts'][0]['text']
            
            # Parse TITLE and CONTENT
            import re
            title_match = re.search(r'TITLE:\s*(.*?)\nCONTENT:', text, re.IGNORECASE | re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()
                content = text[title_match.end():].strip()
                # Clean up title if it has quotes
                title = title.strip('"\'')
                return title, content
            else:
                # Fallback parsing
                lines = text.split('\n')
                title = lines[0].replace('#', '').strip()
                content = '\n'.join(lines[1:]).strip()
                return title, content
        
        print(f"Gemini content generation error: {response.status_code} - {response.text}")
        return f"{topic} - Latest Updates", generate_fallback_content(topic)
        
    except Exception as e:
        print(f"Error generating content with Gemini: {e}")
        return f"{topic} - Latest Updates", generate_fallback_content(topic)


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


def build_markdown_post(title: str, content: str, now_utc: datetime.datetime) -> str:
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
title: "{title}"
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
    
    # Select a new random topic
    topic = random.choice(TOPICS)
    print(f"Selected topic: {topic}")
    
    # Generate content using Gemini
    title, content = generate_blog_content_with_gemini(topic, now_utc)
    print(f"Generated content length: {len(content)} characters")
    
    # Build title and markdown
    slug = slugify(title)
    # Ensure unique filename with timestamp
    file_name = f"{now_utc.strftime('%Y-%m-%d')}-{slug}-{int(now_utc.timestamp())}.md"
    post_path = POSTS_DIR / file_name
    
    # Create and save the post
    post_markdown = build_markdown_post(title, content, now_utc)
    post_path.write_text(post_markdown, encoding="utf-8")
    
    return post_path, title


def main():
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    
    print(f"🤖 AI Blog Generator started at {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
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
