---
layout: default
title: "Documentation Philosophy"
date: 2025-05-12
categories: guide
author: "RK"
description: "Core philosophy behind simple, readable, and maintainable documentation with emphasis on Markdown, scalability, and practicality."
keywords: ["documentation philosophy", "documentation principles", "Markdown philosophy", "simple documentation", "readable source text", "scalable documentation", "minimum viable documentation", "incremental improvement", "technical writing philosophy", "documentation best practices"]
tags: ["documentation", "philosophy", "markdown", "technical-writing", "best-practices", "readability", "simplicity", "incremental-improvement", "developer-docs", "content-authoring"]
---


# Philosophy

*Clay becomes pottery through craft, but it's the emptiness that makes a pot
useful.*

Contents:

1.  [Radical simplicity](#radical-simplicity)
1.  [Readable source text](#readable-source-text)
1.  [Minimum viable documentation](#minimum-viable-documentation)
1.  [Better is better than best](#better-is-better-than-best)

## Radical simplicity

*   **Scalability and interoperability** are more important than a menagerie of
    unessential features. Scale comes from simplicity, speed, and ease.
    Interoperability comes from unadorned, digestible content.

*   **Fewer distractions** make for better writing and more productive reading.

*   **New features should never interfere with the simplest use case** and
    should remain invisible to users who don't need them.

*   **Markdown is designed for the average engineer** -- the busy,
    just-want-to-go-back-to-coding engineer. Large and complex documentation is
    possible but not the primary focus.

*   **Minimizing context switching makes people happier.** Engineers should be
    able to interact with documentation using the same tools they use to read
    and write code.

## Readable source text

* **Plain text not only suffices, it is superior**. Markdown itself is not
  essential to this formula, but it is the best and most widely supported
  solution right now. HTML is generally not encouraged.

* **Content and presentation should not mingle**. It should always be possible
  to ditch the renderer and read the essential information at source. Users
  should never have to touch the presentation layer if they don't want to.

* **Portability and future-proofing leave room for the unimagined integrations
  to come**, and are best achieved by keeping the source as human-readable as
  possible.

* **Static content is better than dynamic**, because content should not depend
  on the features of any one server. However, **fresh is better than stale**. We
  strive to balance these needs.

## Minimum viable documentation

* **Docs thrive when they're treated like tests**: a necessary chore one learns
  to savor because it rewards over time.
  See [Best Practices](best_practices.md).

* **Brief and utilitarian is better than long and exhaustive**. The vast
  majority of users need only a small fraction of the author's total knowledge,
  but they need it quickly and often.

## Better is better than best

*   **Incremental improvement is better than prolonged debate**. Patience and
    tolerance of imperfection allow projects to evolve organically.

*   **Don't
    pass the plate**. Ideas are cheap. We're drowning in potentially impactful
    projects. Choose only those you can really handle and release those you
    can't.
