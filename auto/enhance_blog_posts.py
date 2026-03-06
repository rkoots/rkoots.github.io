import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
DEFAULT_POSTS_DIR = ROOT_DIR / "blog" / "_posts"


def humanize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title).strip().rstrip(" .!?")

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into",
    "is", "it", "its", "of", "on", "or", "the", "to", "with", "your", "you", "this",
    "that", "these", "those", "their", "how", "what", "why", "when", "best", "latest",
    "new", "more", "than", "vs", "will", "can", "now", "after", "before"
}

TOPIC_CONTEXT = {
    "ai": "AI adoption is moving from experimentation to production, which means readers increasingly care about reliability, governance, real-world impact, and measurable business value.",
    "artificial intelligence": "Artificial intelligence is no longer just a research topic. It now shapes product design, customer support, automation, analytics, and decision-making across industries.",
    "healthcare": "Healthcare readers usually want both optimism and realism, especially around patient safety, privacy, workflow integration, and outcomes.",
    "5g": "The 5G conversation is about more than speed. The real value comes from low latency, device density, and the infrastructure needed to support connected services at scale.",
    "github": "Developer productivity content performs best when it combines practical workflow advice with clear examples and common pitfalls.",
    "git": "Git content tends to rank better when it helps readers solve day-to-day workflow problems rather than only listing commands.",
    "seo": "Search visibility now depends on both traditional keyword targeting and how clearly content answers user intent across search, AI summaries, and discovery surfaces.",
    "aeo": "Answer engine optimization focuses on making content easier for AI assistants and search features to interpret, summarize, and cite.",
    "geo": "Generative engine optimization emphasizes structured, trustworthy content that can be surfaced accurately by AI-powered discovery systems.",
    "money": "Personal finance readers respond well to concrete frameworks, realistic examples, and advice that reduces complexity rather than increasing it.",
    "security": "Security-focused readers typically want practical guidance, clear risks, and examples of what can go wrong without becoming overly alarmist.",
    "api": "API content becomes more useful when it connects technical concepts to reliability, security, developer experience, and lifecycle management."
}

AUTHORITATIVE_LINKS = {
    "ai": ("OECD AI policy observatory", "https://oecd.ai/"),
    "artificial intelligence": ("NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
    "healthcare": ("World Health Organization digital health resources", "https://www.who.int/health-topics/digital-health"),
    "5g": ("GSMA 5G insights", "https://www.gsma.com/"),
    "github": ("GitHub documentation", "https://docs.github.com/"),
    "git": ("Git documentation", "https://git-scm.com/doc"),
    "seo": ("Google Search Central", "https://developers.google.com/search"),
    "aeo": ("Google Search Central", "https://developers.google.com/search"),
    "geo": ("Google Search Central", "https://developers.google.com/search"),
    "money": ("Investor.gov financial basics", "https://www.investor.gov/"),
    "security": ("OWASP foundation", "https://owasp.org/"),
    "api": ("OWASP API Security Project", "https://owasp.org/www-project-api-security/")
}

IMAGE_HINTS = {
    "ai": ("Suggested image", "A clean illustration showing AI systems assisting human workflows across software, healthcare, and analytics environments."),
    "healthcare": ("Suggested infographic", "A patient-care workflow diagram showing where AI supports diagnosis, triage, treatment planning, and follow-up."),
    "5g": ("Suggested diagram", "A network diagram comparing 4G and 5G in terms of latency, bandwidth, connected devices, and industry use cases."),
    "git": ("Suggested image", "A developer workflow graphic showing local changes, staging, commits, branches, merge, and push to remote."),
    "github": ("Suggested image", "A visual GitHub workflow with repositories, pull requests, code review, Actions, and deployments."),
    "seo": ("Suggested infographic", "A funnel diagram showing SEO, AEO, and GEO working together across search engines, AI answers, and content discovery."),
    "money": ("Suggested infographic", "A personal finance dashboard with budgeting, saving, debt reduction, investing, and emergency fund tracking."),
    "security": ("Suggested diagram", "A layered security model highlighting authentication, authorization, rate limiting, validation, monitoring, and incident response."),
    "api": ("Suggested diagram", "An API lifecycle diagram covering design, authentication, validation, observability, versioning, and deprecation."),
}


def parse_front_matter(text: str) -> Tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text.strip()
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return "", text.strip()
    return parts[1].strip(), parts[2].strip()



def extract_field(front_matter: str, field: str) -> str:
    match = re.search(rf"^{field}:\s*(.+)$", front_matter, re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip().strip('"')



def extract_list_field(front_matter: str, field: str) -> List[str]:
    raw = extract_field(front_matter, field)
    if not raw:
        return []
    if raw.startswith("[") and raw.endswith("]"):
        items = [item.strip().strip('"\'') for item in raw[1:-1].split(",") if item.strip()]
        return [item for item in items if item]
    return [raw]



def normalize_title_from_filename(path: Path) -> str:
    stem = path.stem
    normalized = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)
    normalized = normalized.replace("-", " ").replace("_", " ")
    return normalized.strip().title()



def extract_keywords(title: str, tags: List[str], body: str) -> List[str]:
    prioritized = [tag.lower().strip() for tag in tags if tag.strip()]
    candidates = re.findall(r"[A-Za-z0-9+#]{2,}", " ".join([title, " ".join(tags), body[:1200]]))
    seen = []
    for token in prioritized + [token.lower() for token in candidates]:
        lowered = token.lower()
        if lowered in STOPWORDS:
            continue
        if lowered.isdigit():
            continue
        if lowered not in seen:
            seen.append(lowered)
    return seen[:8]



def summarize_existing_content(body: str, title: str) -> str:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    text_paragraphs = [p for p in paragraphs if not p.startswith("#") and not p.startswith("![") and not p.startswith("```")]
    title_label = humanize_title(title)
    if text_paragraphs:
        source = text_paragraphs[0]
        source = re.sub(r"\s+", " ", source)
        if len(source) > 180:
            source = source[:180].rstrip(" ,.;:")
        return f"{title_label} remains a relevant topic because it influences how people evaluate technology, risk, opportunity, and long-term change. This article expands the discussion with clearer context and practical meaning for readers."
    return f"{title_label} is a useful topic for readers who want more than a quick summary. The goal of this article is to explain the core idea clearly and connect it to practical decisions and broader context."



def build_key_takeaways(title: str, body: str, keywords: List[str]) -> List[str]:
    takeaways = []
    title_label = humanize_title(title)
    if re.search(r"challenge|risk|concern|privacy|security|cost", body, re.IGNORECASE):
        takeaways.append(f"{title_label} is not only about opportunity. It also involves execution challenges, trade-offs, and real-world constraints that readers should understand.")
    if re.search(r"industry|market|business|developer|workflow|team", body, re.IGNORECASE):
        takeaways.append("The most useful lens for this topic is practical impact: how it changes decisions, operations, or user experience in real settings.")
    if keywords:
        takeaways.append(f"Readers interested in {', '.join(keywords[:3])} should look beyond headlines and focus on long-term adoption, measurable benefits, and implementation details.")
    if not takeaways:
        takeaways.append("The core value of this topic becomes clearer when it is connected to real use cases, examples, and likely next steps.")
    while len(takeaways) < 3:
        takeaways.append("A strong understanding of the basics makes it much easier to evaluate hype, compare options, and make better decisions.")
    return takeaways[:3]



def build_context_paragraph(keywords: List[str], title: str) -> str:
    for keyword in keywords:
        if keyword in TOPIC_CONTEXT:
            return TOPIC_CONTEXT[keyword]
    title_label = humanize_title(title).lower()
    return f"For many readers, the real question behind {title_label} is not simply what it is, but how it affects daily decisions, future opportunities, and the broader market or technology landscape."



def build_examples_section(keywords: List[str], title: str) -> str:
    if "5g" in keywords:
        return (
            "A simple way to think about 5G is to compare it to upgrading from a single-lane road to a smart traffic system. "
            "It is not just faster movement; it is better coordination, less delay, and more capacity for many vehicles at once. "
            "That is why industries such as logistics, smart manufacturing, and connected healthcare are paying attention."
        )
    if "healthcare" in keywords or "ai" in keywords:
        return (
            "Consider a hospital triage workflow: if clinicians must review thousands of scans or records manually, delays are unavoidable. "
            "AI does not replace expert judgment, but it can help prioritize cases, flag anomalies, and surface patterns earlier, allowing teams to focus attention where it matters most."
        )
    if "git" in keywords or "github" in keywords:
        return (
            "A practical example is a feature branch workflow. A developer creates a branch, makes a focused change, reviews the diff, opens a pull request, and merges only after feedback. "
            "That process improves traceability, reduces risk, and helps teams collaborate without stepping on each other’s work."
        )
    if "money" in keywords:
        return (
            "Think of personal finance like physical fitness. Crash diets rarely create lasting health, and one-time money hacks rarely create lasting wealth. "
            "What works better is a repeatable system of budgeting, saving, reviewing, and adjusting over time."
        )
    if "seo" in keywords or "aeo" in keywords or "geo" in keywords:
        return (
            "A useful case study is a technical article that ranks modestly in traditional search but is written with clear headings, direct answers, and trustworthy references. "
            "That structure can improve its chances of appearing in search snippets, AI summaries, and broader content recommendation systems."
        )
    title_label = humanize_title(title).lower()
    return (
        f"One useful way to evaluate {title_label} is to ask what changes for users, teams, or customers after adoption. "
        "If the answer is clearer workflows, faster decisions, lower risk, or better outcomes, the topic usually has lasting relevance beyond short-term buzz."
    )



def build_image_block(title: str, keywords: List[str]) -> str:
    for keyword in keywords:
        if keyword in IMAGE_HINTS:
            label, alt = IMAGE_HINTS[keyword]
            caption = f"{label}: visual support for the article '{title}' to improve readability and shareability."
            return f"> **{label}:** {alt}\n> **Alt text:** {alt}\n> **Caption:** {caption}"
    alt = f"Editorial illustration related to {title}"
    return f"> **Suggested image:** A clean, publication-style hero image related to {title.lower()}.\n> **Alt text:** {alt}\n> **Caption:** Visual summary supporting the main ideas discussed in the article."



def build_authority_link(keywords: List[str]) -> str:
    for keyword in keywords:
        if keyword in AUTHORITATIVE_LINKS:
            label, url = AUTHORITATIVE_LINKS[keyword]
            return f"- **Authoritative reference:** [{label}]({url})"
    return "- **Authoritative reference:** [Google Search Central](https://developers.google.com/search)"



def build_internal_link_suggestions(path: Path, title: str, all_posts: List[Path]) -> str:
    current_terms = set(re.findall(r"[a-z0-9]+", title.lower())) - STOPWORDS
    related = []
    for candidate in all_posts:
        if candidate == path:
            continue
        candidate_title = normalize_title_from_filename(candidate)
        terms = set(re.findall(r"[a-z0-9]+", candidate_title.lower())) - STOPWORDS
        overlap = current_terms.intersection(terms)
        if overlap:
            slug = candidate.stem
            related.append((len(overlap), candidate_title, f"/blog/{slug.replace(' ', '-').lower()}.html"))
    related.sort(key=lambda item: (-item[0], item[1]))
    lines = []
    for _, related_title, url in related[:3]:
        lines.append(f"- **Related post:** [{related_title}]({url})")
    if not lines:
        lines.append("- **Related post:** Browse more articles in the [blog archive](/blog/)")
    return "\n".join(lines)



def body_has_section(body: str, heading: str) -> bool:
    return heading.lower() in body.lower()



def clean_body(body: str) -> str:
    body = body.strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body



def enhance_body(path: Path, title: str, body: str, tags: List[str], all_posts: List[Path]) -> str:
    body = clean_body(body)
    keywords = extract_keywords(title, tags, body)
    intro = summarize_existing_content(body, title)
    takeaways = build_key_takeaways(title, body, keywords)
    context = build_context_paragraph(keywords, title)
    examples = build_examples_section(keywords, title)
    image_block = build_image_block(title, keywords)
    links_block = build_internal_link_suggestions(path, title, all_posts)
    authority_link = build_authority_link(keywords)

    sections: List[str] = []

    if not body_has_section(body, "In This Article"):
        sections.append("## In This Article\n\n" + "\n".join([f"- {item}" for item in [
            "A clear overview of the topic",
            "Why it matters right now",
            "Practical context, examples, and risks",
            "Suggested visuals and related reading"
        ]]))

    if not body_has_section(body, "Why This Topic Matters"):
        sections.append(f"## Why This Topic Matters\n\n{context}")

    if not body_has_section(body, "Key Takeaways"):
        sections.append("## Key Takeaways\n\n" + "\n".join([f"- {item}" for item in takeaways]))

    if not re.match(r"^#{1,6}\s", body):
        rebuilt_body = f"## Overview\n\n{intro}\n\n{body}"
    else:
        rebuilt_body = f"## Overview\n\n{intro}\n\n{body}"

    if not body_has_section(body, "Practical Example") and not body_has_section(body, "Real-World"):
        sections.append(f"## Practical Example and Reader Context\n\n{examples}")

    if "![" not in body:
        sections.append(f"## Visual Suggestion\n\n{image_block}")

    if not body_has_section(body, "Further Reading") and not body_has_section(body, "References"):
        sections.append(f"## Further Reading and Related Resources\n\n{links_block}\n{authority_link}")

    if not body_has_section(body, "Final Thoughts") and not body_has_section(body, "Conclusion"):
        title_label = humanize_title(title)
        sections.append(
            "## Final Thoughts\n\n"
            f"The core ideas behind {title_label} become much more useful when readers connect them to outcomes, trade-offs, and implementation realities. "
            "A well-structured understanding helps cut through hype and supports better decisions over time."
        )

    return rebuilt_body + "\n\n" + "\n\n".join(section for section in sections if section).strip() + "\n"



def ensure_description(front_matter: str, body: str, title: str) -> str:
    if re.search(r"^description:\s*.+$", front_matter, re.MULTILINE):
        return front_matter
    summary = summarize_existing_content(body, title)
    description = summary[:155].rstrip(" .") + "."
    return front_matter + f"\ndescription: \"{description}\""



def process_post(path: Path, all_posts: List[Path], apply_changes: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    front_matter, body = parse_front_matter(original)
    if not front_matter:
        return False
    title = extract_field(front_matter, "title") or normalize_title_from_filename(path)
    tags = extract_list_field(front_matter, "tags")
    updated_front_matter = ensure_description(front_matter, body, title)
    updated_body = enhance_body(path, title, body, tags, all_posts)
    updated = f"---\n{updated_front_matter}\n---\n\n{updated_body}"
    if updated == original:
        return False
    if apply_changes:
        path.write_text(updated, encoding="utf-8")
    return True



def main() -> None:
    parser = argparse.ArgumentParser(description="Enhance Markdown blog posts with consistent editorial structure.")
    parser.add_argument("--posts-dir", default=str(DEFAULT_POSTS_DIR), help="Directory containing markdown posts")
    parser.add_argument("--limit", type=int, default=0, help="Optional limit for number of posts to process")
    parser.add_argument("--apply", action="store_true", help="Write changes to files. Without this flag, runs in preview mode.")
    args = parser.parse_args()

    posts_dir = Path(args.posts_dir)
    posts = sorted(posts_dir.glob("*.md"))
    if args.limit > 0:
        posts = posts[:args.limit]

    changed = 0
    for post in posts:
        if process_post(post, posts, args.apply):
            changed += 1
            print(f"UPDATED: {post.name}")
        else:
            print(f"SKIPPED: {post.name}")

    mode = "APPLY" if args.apply else "PREVIEW"
    print(f"{mode} COMPLETE - processed={len(posts)} changed={changed}")


if __name__ == "__main__":
    main()
