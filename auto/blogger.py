import datetime
import os
import re
from pathlib import Path
from typing import Tuple

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/blogger"]

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
POSTS_DIR = ROOT_DIR / "blog" / "_posts"
TOKEN_FILE = BASE_DIR / "token.json"

BLOG_ID = os.getenv("BLOG_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BLOGGER_REFRESH_TOKEN = os.getenv("BLOGGER_REFRESH_TOKEN")

PUBLISH_TO_BLOGGER = os.getenv("PUBLISH_TO_BLOGGER", "false").lower() == "true"
FORCE_RUN = os.getenv("FORCE_RUN", "false").lower() == "true"


def is_publish_day(now_utc: datetime.datetime) -> bool:
    # Wednesday=2, Friday=4
    return now_utc.weekday() in {2, 4}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\s-]", "", value.lower()).strip()
    return re.sub(r"[\s_-]+", "-", slug)


def build_title(now_utc: datetime.datetime) -> str:
    return f"Engineering & AI Weekly Brief - {now_utc.strftime('%d %b %Y')}"


def build_markdown_post(now_utc: datetime.datetime, title: str) -> str:
    date_str = now_utc.strftime("%Y-%m-%d")
    pub_str = now_utc.strftime("%Y-%m-%d %H:%M UTC")
    return f"""---
layout: default
title: \"{title}\"
date: {date_str}
author: Rajkumar V.
categories: [Engineering, AI, Weekly]
tags: [AI, Engineering Leadership, Productivity, Architecture]
description: Weekly deep-dive on engineering trends, architecture patterns, AI adoption, and practical execution guidance.
---

## Executive Summary

Published on **{pub_str}**, this edition focuses on practical ways engineering teams can convert AI experimentation into measurable product outcomes.

- **Signal 1:** Teams that define explicit quality guardrails for AI features ship faster with fewer rollbacks.
- **Signal 2:** Retrieval-first architectures continue to outperform pure prompt-only approaches in enterprise workflows.
- **Signal 3:** Weekly technical debt checkpoints improve release confidence for AI-infused products.

## This Week's Deep Dive: Production AI for Engineering Teams

### 1) Architecture Decisions That Age Well

When introducing AI features, prioritize:

1. **Observability from day one** (latency, failure modes, token usage, cost per request)
2. **Fallback paths** for model outage or degraded quality
3. **Versioned prompts and evaluators** so behavior changes are traceable

### 2) Delivery Playbook for Leads and Staff Engineers

Use this cadence for each AI feature:

- **Monday:** Problem framing + baseline metric definition
- **Tuesday/Wednesday:** Controlled implementation in staging with test cohorts
- **Thursday:** Quality eval (hallucination, consistency, relevance)
- **Friday:** Rollout decision with clear rollback trigger

### 3) Quality Checklist Before Release

- [ ] Latency SLO is defined and measured
- [ ] Response safety filter is active
- [ ] Fallback response path is tested
- [ ] Prompt + model version is logged
- [ ] Stakeholder acceptance criteria are signed off

## What Engineering Leaders Should Track

### Core KPI Trio

1. **Time-to-Value**: How quickly users receive useful output
2. **Reliability Score**: Success rate under normal and stress conditions
3. **Iteration Velocity**: Number of validated improvements per release cycle

### Common Pitfalls Seen in Teams

- Shipping AI features without deterministic post-processing
- Ignoring data freshness in retrieval pipelines
- Over-optimizing model choice before improving context quality

## Action Plan for the Next 7 Days

1. Choose one production workflow that can be improved by AI assistance.
2. Instrument baseline metrics (time, quality, error rate).
3. Deploy a small controlled experiment to a subset of users.
4. Capture measurable outcomes and publish learnings internally.

## Closing Thoughts

Engineering excellence in AI products is rarely about one perfect model. It comes from disciplined architecture, measurable iteration, and reliable operational practices. Keep the bar high, ship in small loops, and optimize with data.
"""


def build_blogger_html(now_utc: datetime.datetime, title: str) -> str:
    pub_str = now_utc.strftime("%Y-%m-%d %H:%M UTC")
    return f"""
<h2>{title}</h2>
<p><strong>Published:</strong> {pub_str}</p>

<h3>Executive Summary</h3>
<ul>
  <li>Define quality guardrails early to reduce AI rollout risk.</li>
  <li>Use retrieval + validation workflows for better production reliability.</li>
  <li>Track measurable KPIs weekly and iterate in short loops.</li>
</ul>

<h3>Deep Dive</h3>
<p>Production-ready AI systems are built on observability, fallback mechanisms, and versioned prompts. Engineering teams that treat AI features like core platform features consistently deliver better outcomes.</p>

<h3>7-Day Action Plan</h3>
<ol>
  <li>Select one workflow to improve with AI assistance.</li>
  <li>Measure baseline quality and latency.</li>
  <li>Run a staged rollout and evaluate with clear acceptance criteria.</li>
  <li>Scale only after reliability and business impact are validated.</li>
</ol>

<p><em>Stay focused on measurable impact, not model hype.</em></p>
""".strip()


def generate_post_file(now_utc: datetime.datetime) -> Tuple[Path, str, str]:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    title = build_title(now_utc)
    slug = slugify(title)
    file_name = f"{now_utc.strftime('%Y-%m-%d')}-{slug}.md"
    post_path = POSTS_DIR / file_name

    post_markdown = build_markdown_post(now_utc, title)
    post_path.write_text(post_markdown, encoding="utf-8")

    return post_path, title, build_blogger_html(now_utc, title)


def authenticate_blogger():
    if not BLOG_ID:
        raise ValueError("Missing BLOG_ID environment variable.")

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not all([CLIENT_ID, CLIENT_SECRET, BLOGGER_REFRESH_TOKEN]):
                raise ValueError(
                    "Missing CLIENT_ID/CLIENT_SECRET/BLOGGER_REFRESH_TOKEN for headless auth."
                )
            creds = Credentials(
                token=None,
                refresh_token=BLOGGER_REFRESH_TOKEN,
                token_uri="https://oauth2.googleapis.com/token",
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                scopes=SCOPES,
            )
            creds.refresh(Request())

        TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")

    return build("blogger", "v3", credentials=creds, cache_discovery=False)


def publish_post(service, title: str, content: str):
    post_body = {"kind": "blogger#post", "title": title, "content": content}
    post = service.posts().insert(blogId=BLOG_ID, body=post_body, isDraft=False).execute()
    print(f"Published to Blogger: {post['url']}")


def main():
    now_utc = datetime.datetime.now(datetime.timezone.utc)

    if not FORCE_RUN and not is_publish_day(now_utc):
        print("Not a Wednesday/Friday run. Skipping generation.")
        return

    post_path, title, blogger_html = generate_post_file(now_utc)
    print(f"Generated post file: {post_path}")

    if PUBLISH_TO_BLOGGER:
        service = authenticate_blogger()
        publish_post(service, title, blogger_html)
    else:
        print("PUBLISH_TO_BLOGGER is false. File generated only.")


if __name__ == "__main__":
    main()
