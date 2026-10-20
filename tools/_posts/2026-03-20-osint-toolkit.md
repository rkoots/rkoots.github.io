---
layout: default
title: "OSINT Hub 2026: The Ultimate Open Source Intelligence Directory & 1,400+ Free Investigation Tools"
subtitle: "1,450+ Verified OSINT Tools, Threat Intel Feeds, Darknet Indices, People Search & OpSec Utilities"
excerpt: "Explore 1,450+ curated Open Source Intelligence (OSINT) tools across 79 categories. Real-time search, SOCMINT trackers, reverse lookups, darknet indexes, and OpSec sandboxes."
date: 2026-03-20
categories: tools
permalink: /tools/osint/
logo_svg: /assets/images/tools/logos/osint.svg
description: "The definitive 2026 Open Source Intelligence (OSINT) toolkit and directory. 1,400+ free investigative tools across 79 categories: SOCMINT, GEOINT, domain recon, people search, darknet, phone lookup, and OpSec sandboxes."
keywords: ["osint tools", "open source intelligence", "osint framework", "best osint tools 2026", "free people search", "reverse phone lookup", "social media osint", "socmint", "geoint tools", "darknet investigation", "threat intelligence feeds", "username search", "email lookup free", "opsec tools", "cyber investigator toolkit", "shodan alternatives"]
tags: [osint, cybersecurity, threat-intelligence, investigation, privacy, socmint, geoint, developer-tools]
og:title: "OSINT Hub 2026: 1,400+ Free Open Source Intelligence Tools"
og:description: "Comprehensive verified directory of 1,450+ OSINT tools, darknet directories, SOCMINT trackers, reverse lookups, and OpSec sandboxes."
og:type: website
og:image: https://rkoots.github.io/assets/images/tools/logos/osint.svg
twitter:card: summary_large_image
twitter:title: "OSINT Hub 2026: 1,400+ Free Open Source Intelligence Tools"
twitter:description: "The ultimate directory of 1,450+ verified OSINT investigation tools for cyber investigators, journalists, and researchers."
---

<!-- Schema.org Microdata for SEO & Rich Snippets -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "name": "OSINT Hub - Open Source Intelligence Toolkit",
      "operatingSystem": "All Web Browsers",
      "applicationCategory": "SecurityApplication",
      "description": "Interactive investigative portal indexing 1,450+ curated OSINT tools across 79 intelligence categories including people search, social media, threat intel, and geospatial forensics.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      },
      "author": {
        "@type": "Person",
        "name": "Rajkumar Venkataraman"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is OSINT (Open Source Intelligence)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "OSINT stands for Open Source Intelligence. It involves collecting, analyzing, and synthesizing publicly available information—such as public databases, social media platforms, government records, DNS registries, and commercial registries—to answer specific investigative questions."
          }
        },
        {
          "@type": "Question",
          "name": "Is OSINT investigation legal and ethical?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, OSINT relies exclusively on legal, publicly available data and does not involve unauthorized access, hacking, or interception. However, ethical investigators must strictly adhere to privacy laws, terms of service, and human rights guidelines."
          }
        },
        {
          "@type": "Question",
          "name": "What are the most essential OSINT tools for beginners?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Beginner researchers should start with multi-purpose tools like CyberChef for data decoding, Wayback Machine and Archive.is for web preservation, Google Dorks for targeted indexing, WhatsMyName for username enumeration, and Epieos for email address verification."
          }
        },
        {
          "@type": "Question",
          "name": "How can I maintain OpSec (Operational Security) while investigating?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Always isolate your research environment using virtual sandboxes (such as Kasm or virtual machines), separate research browsers with anti-fingerprinting, burner phone numbers/SMS services for account creation, and encrypted VPN/Tor routing."
          }
        }
      ]
    }
  ]
}
</script>

<style>
/* ==========================================================================
   OSINT TOOLKIT - NIGHT DETAIL & MODERN CYBER AESTHETICS
   ========================================================================== */
:root {
  --os-bg: #070b14;
  --os-surface: #0d1527;
  --os-surface-hover: #13203b;
  --os-card: #0f1a30;
  --os-border: rgba(56, 189, 248, 0.16);
  --os-border-glow: rgba(56, 189, 248, 0.35);
  --os-cyan: #06b6d4;
  --os-cyan-bright: #38bdf8;
  --os-purple: #8b5cf6;
  --os-purple-bright: #a855f7;
  --os-emerald: #10b981;
  --os-amber: #f59e0b;
  --os-red: #ef4444;
  --os-text: #f8fafc;
  --os-text-muted: #94a3b8;
  --os-text-dim: #64748b;
  --os-shadow: 0 10px 30px -10px rgba(2, 6, 23, 0.7);
  --os-glow: 0 0 25px rgba(6, 182, 212, 0.22);
  --os-radius-sm: 8px;
  --os-radius-md: 14px;
  --os-radius-lg: 20px;
  --os-font-mono: 'JetBrains Mono', Consolas, 'Courier New', monospace;
  --os-font-sans: 'Inter', system-ui, -apple-system, sans-serif;
}

/* Light Theme Switcher override */
body.daylight-lab {
  --os-bg: #f8fafc;
  --os-surface: #ffffff;
  --os-surface-hover: #f1f5f9;
  --os-card: #ffffff;
  --os-border: #cbd5e1;
  --os-border-glow: #38bdf8;
  --os-text: #0f172a;
  --os-text-muted: #475569;
  --os-text-dim: #64748b;
  --os-shadow: 0 10px 30px -10px rgba(100, 116, 139, 0.15);
  --os-glow: 0 0 20px rgba(6, 182, 212, 0.15);
}

.osint-wrapper {
  background: var(--os-bg);
  color: var(--os-text);
  font-family: var(--os-font-sans);
  min-height: 100vh;
  margin: -30px -15px 0;
  padding: 30px 20px 80px;
  position: relative;
  overflow-x: hidden;
  transition: background 0.3s ease, color 0.3s ease;
}

/* Subtle Matrix Grid & Glow backdrop */
.osint-wrapper::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 600px;
  background: 
    radial-gradient(circle at 50% 50px, rgba(56, 189, 248, 0.12) 0%, transparent 60%),
    radial-gradient(circle at 85% 180px, rgba(139, 92, 246, 0.09) 0%, transparent 50%),
    linear-gradient(rgba(56, 189, 248, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(56, 189, 248, 0.03) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 32px 32px, 32px 32px;
  pointer-events: none;
  z-index: 0;
}

.osint-container {
  max-width: 1400px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

/* HERO SECTION */
.osint-hero {
  text-align: center;
  padding: 40px 20px 32px;
  margin-bottom: 24px;
  position: relative;
}

.osint-hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(6, 182, 212, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.3);
  color: var(--os-cyan-bright);
  padding: 6px 18px;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-bottom: 18px;
  box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
}

.live-pulse {
  width: 8px;
  height: 8px;
  background: var(--os-emerald);
  border-radius: 50%;
  box-shadow: 0 0 10px var(--os-emerald);
  animation: pulseDot 2s infinite ease-in-out;
}

@keyframes pulseDot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.4); opacity: 0.6; }
}

.osint-hero h1 {
  font-size: clamp(2rem, 4.5vw, 3.2rem);
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 16px;
  color: #ffffff;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #ffffff 40%, var(--os-cyan-bright) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

body.daylight-lab .osint-hero h1 {
  background: linear-gradient(135deg, #0f172a 40%, #0284c7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.osint-hero-lead {
  font-size: clamp(1rem, 1.8vw, 1.25rem);
  color: var(--os-text-muted);
  max-width: 850px;
  margin: 0 auto 28px;
  line-height: 1.6;
}

/* KPI STATS ROW */
.osint-stats-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 32px;
}

.kpi-pill {
  background: var(--os-surface);
  border: 1px solid var(--os-border);
  padding: 10px 20px;
  border-radius: var(--os-radius-md);
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 0.9rem;
  box-shadow: var(--os-shadow);
  transition: transform 0.2s, border-color 0.2s;
}

.kpi-pill:hover {
  transform: translateY(-2px);
  border-color: var(--os-cyan-bright);
}

.kpi-num {
  font-size: 1.25rem;
  font-weight: 800;
  font-family: var(--os-font-mono);
  color: var(--os-cyan-bright);
}

.kpi-lbl {
  color: var(--os-text-muted);
  font-weight: 500;
}

/* RECON QUICK PIVOT CONSOLE */
.recon-console {
  background: linear-gradient(135deg, rgba(13, 21, 39, 0.9), rgba(15, 26, 48, 0.95));
  border: 1px solid var(--os-border);
  border-radius: var(--os-radius-lg);
  padding: 24px;
  margin-bottom: 36px;
  box-shadow: var(--os-shadow), var(--os-glow);
  backdrop-filter: blur(12px);
}

.recon-console-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  flex-wrap: wrap;
  gap: 12px;
}

.recon-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--os-cyan-bright);
  display: flex;
  align-items: center;
  gap: 10px;
}

.recon-title i {
  color: var(--os-cyan);
}

.recon-badge {
  font-size: 0.75rem;
  background: rgba(139, 92, 246, 0.2);
  color: var(--os-purple-bright);
  padding: 4px 10px;
  border-radius: 999px;
  font-weight: 600;
  border: 1px solid rgba(139, 92, 246, 0.4);
}

.recon-input-wrap {
  display: flex;
  gap: 10px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.recon-target-input {
  flex: 1;
  min-width: 280px;
  background: rgba(7, 11, 20, 0.85);
  border: 2px solid var(--os-border);
  color: #ffffff;
  padding: 14px 18px;
  border-radius: var(--os-radius-md);
  font-family: var(--os-font-mono);
  font-size: 1rem;
  transition: all 0.25s;
}

.recon-target-input:focus {
  outline: none;
  border-color: var(--os-cyan-bright);
  box-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
  background: rgba(7, 11, 20, 1);
}

.recon-buttons {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.pivot-btn {
  background: var(--os-surface);
  border: 1px solid var(--os-border);
  color: var(--os-text);
  padding: 10px 16px;
  border-radius: var(--os-radius-sm);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
  text-decoration: none;
}

.pivot-btn:hover {
  background: var(--os-cyan);
  color: #070b14;
  border-color: var(--os-cyan-bright);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(6, 182, 212, 0.35);
}

/* TOOLBAR: SEARCH, CATEGORIES & CONTROLS */
.osint-toolbar {
  background: var(--os-surface);
  border: 1px solid var(--os-border);
  border-radius: var(--os-radius-lg);
  padding: 20px;
  margin-bottom: 30px;
  box-shadow: var(--os-shadow);
  position: sticky;
  top: 15px;
  z-index: 100;
  backdrop-filter: blur(16px);
}

.toolbar-primary {
  display: flex;
  gap: 14px;
  align-items: center;
  margin-bottom: 18px;
  flex-wrap: wrap;
}

.search-container {
  position: relative;
  flex: 1;
  min-width: 280px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--os-text-dim);
  font-size: 1.1rem;
}

.osint-search-input {
  width: 100%;
  padding: 14px 44px 14px 46px;
  background: rgba(7, 11, 20, 0.7);
  border: 2px solid var(--os-border);
  border-radius: var(--os-radius-md);
  color: #ffffff;
  font-size: 1rem;
  font-family: var(--os-font-sans);
  transition: all 0.25s;
}

.osint-search-input:focus {
  outline: none;
  border-color: var(--os-cyan-bright);
  box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
  background: rgba(7, 11, 20, 0.95);
}

body.daylight-lab .osint-search-input {
  background: #ffffff;
  color: #0f172a;
}

.clear-search-btn {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  color: var(--os-text-dim);
  font-size: 1rem;
  cursor: pointer;
  display: none;
}

.clear-search-btn:hover {
  color: var(--os-cyan-bright);
}

.toolbar-controls {
  display: flex;
  gap: 10px;
  align-items: center;
  flex-wrap: wrap;
}

.select-wrap select {
  background: rgba(7, 11, 20, 0.7);
  border: 1px solid var(--os-border);
  color: var(--os-text);
  padding: 12px 16px;
  border-radius: var(--os-radius-md);
  font-size: 0.9rem;
  cursor: pointer;
  font-weight: 500;
  outline: none;
  transition: border-color 0.2s;
}

body.daylight-lab .select-wrap select {
  background: #ffffff;
}

.select-wrap select:focus {
  border-color: var(--os-cyan-bright);
}

.btn-icon-toggle {
  background: rgba(7, 11, 20, 0.7);
  border: 1px solid var(--os-border);
  color: var(--os-text-muted);
  width: 44px;
  height: 44px;
  border-radius: var(--os-radius-md);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 1.1rem;
}

.btn-icon-toggle:hover, .btn-icon-toggle.active {
  background: var(--os-cyan);
  color: #070b14;
  border-color: var(--os-cyan-bright);
}

.btn-action {
  background: var(--os-surface-hover);
  border: 1px solid var(--os-border);
  color: var(--os-text);
  padding: 11px 16px;
  border-radius: var(--os-radius-md);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
}

.btn-action:hover {
  background: var(--os-cyan);
  color: #070b14;
  border-color: var(--os-cyan-bright);
}

.btn-action.btn-random {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(6, 182, 212, 0.2));
  border-color: var(--os-purple);
  color: var(--os-cyan-bright);
}

.btn-action.btn-random:hover {
  background: linear-gradient(135deg, var(--os-purple), var(--os-cyan));
  color: #ffffff;
}

/* DOMAIN GROUP TABS */
.domain-tabs-scroll {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 4px;
  scrollbar-width: thin;
}

.domain-tab {
  background: rgba(7, 11, 20, 0.5);
  border: 1px solid var(--os-border);
  color: var(--os-text-muted);
  padding: 8px 16px;
  border-radius: 999px;
  font-size: 0.85rem;
  font-weight: 600;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.domain-tab:hover {
  color: var(--os-cyan-bright);
  border-color: var(--os-cyan-bright);
  background: rgba(56, 189, 248, 0.08);
}

.domain-tab.active {
  background: linear-gradient(135deg, var(--os-cyan), #0284c7);
  color: #ffffff;
  border-color: var(--os-cyan-bright);
  box-shadow: 0 2px 10px rgba(6, 182, 212, 0.4);
}

.domain-tab-count {
  font-size: 0.75rem;
  padding: 2px 6px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.2);
  color: inherit;
}

.domain-tab.active .domain-tab-count {
  background: rgba(0, 0, 0, 0.25);
  color: #ffffff;
}

/* RESULTS META BAR */
.results-meta-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid rgba(56, 189, 248, 0.1);
  font-size: 0.85rem;
  color: var(--os-text-muted);
}

.results-count strong {
  color: var(--os-cyan-bright);
  font-family: var(--os-font-mono);
}

/* TOOLS GRID CONTAINER */
.tools-grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.tools-grid-container.list-mode {
  grid-template-columns: 1fr;
  gap: 12px;
}

/* CARD STYLES */
.osint-card {
  background: var(--os-card);
  border: 1px solid var(--os-border);
  border-radius: var(--os-radius-md);
  padding: 20px;
  display: flex;
  flex-direction: column;
  transition: all 0.25s ease;
  position: relative;
  box-shadow: var(--os-shadow);
}

.osint-card:hover {
  border-color: var(--os-cyan-bright);
  transform: translateY(-4px);
  box-shadow: 0 12px 30px -10px rgba(6, 182, 212, 0.25);
}

.osint-card.highlight-pulse {
  animation: cardHighlight 2s ease-in-out infinite;
}

@keyframes cardHighlight {
  0%, 100% { box-shadow: 0 0 25px var(--os-cyan-bright); border-color: var(--os-cyan-bright); }
  50% { box-shadow: 0 0 40px var(--os-purple-bright); border-color: var(--os-purple-bright); }
}

.card-top {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 12px;
}

.tool-icon-frame {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  background: rgba(7, 11, 20, 0.6);
  border: 1px solid var(--os-border);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
}

.tool-icon-img {
  width: 24px;
  height: 24px;
  object-fit: contain;
}

.tool-icon-fallback {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--os-cyan-bright);
  font-family: var(--os-font-mono);
}

.card-header-info {
  flex: 1;
  min-width: 0;
}

.tool-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 4px 0;
  line-height: 1.3;
  display: flex;
  align-items: center;
  gap: 6px;
}

body.daylight-lab .tool-name {
  color: #0f172a;
}

.tool-name a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s;
}

.tool-name a:hover {
  color: var(--os-cyan-bright);
}

.tool-domain {
  font-size: 0.75rem;
  font-family: var(--os-font-mono);
  color: var(--os-text-dim);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.btn-star {
  background: transparent;
  border: none;
  color: var(--os-text-dim);
  font-size: 1.15rem;
  cursor: pointer;
  padding: 4px;
  transition: all 0.2s;
}

.btn-star:hover, .btn-star.starred {
  color: #eab308;
  transform: scale(1.15);
}

.card-badges {
  display: flex;
  gap: 6px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.badge-tag {
  font-size: 0.7rem;
  padding: 3px 8px;
  border-radius: 6px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.badge-group {
  background: rgba(139, 92, 246, 0.15);
  color: var(--os-purple-bright);
  border: 1px solid rgba(139, 92, 246, 0.3);
}

.badge-cat {
  background: rgba(6, 182, 212, 0.12);
  color: var(--os-cyan-bright);
  border: 1px solid rgba(6, 182, 212, 0.25);
}

.tool-desc {
  font-size: 0.88rem;
  color: var(--os-text-muted);
  line-height: 1.5;
  margin-bottom: 18px;
  flex: 1;
}

.card-actions {
  display: flex;
  gap: 8px;
  margin-top: auto;
  border-top: 1px solid rgba(56, 189, 248, 0.08);
  padding-top: 14px;
}

.card-btn {
  padding: 8px 14px;
  border-radius: var(--os-radius-sm);
  font-size: 0.8rem;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.card-btn-visit {
  flex: 1;
  background: linear-gradient(135deg, var(--os-cyan), #0284c7);
  color: #ffffff;
  border: none;
}

.card-btn-visit:hover {
  background: linear-gradient(135deg, var(--os-cyan-bright), var(--os-cyan));
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(6, 182, 212, 0.35);
}

.card-btn-copy {
  background: rgba(7, 11, 20, 0.6);
  border: 1px solid var(--os-border);
  color: var(--os-text-muted);
}

.card-btn-copy:hover {
  color: var(--os-cyan-bright);
  border-color: var(--os-cyan-bright);
}

/* LIST MODE ADJUSTMENTS */
.tools-grid-container.list-mode .osint-card {
  flex-direction: row;
  align-items: center;
  gap: 20px;
  padding: 14px 20px;
}

.tools-grid-container.list-mode .card-top {
  margin-bottom: 0;
  width: 280px;
}

.tools-grid-container.list-mode .tool-desc {
  margin-bottom: 0;
}

.tools-grid-container.list-mode .card-actions {
  margin-top: 0;
  border-top: none;
  padding-top: 0;
  width: 220px;
}

/* LOAD MORE BUTTON */
.load-more-section {
  text-align: center;
  margin: 30px 0 50px;
}

.btn-load-more {
  background: var(--os-surface);
  border: 2px solid var(--os-cyan-bright);
  color: var(--os-cyan-bright);
  padding: 14px 32px;
  border-radius: var(--os-radius-md);
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  transition: all 0.25s;
}

.btn-load-more:hover {
  background: var(--os-cyan);
  color: #070b14;
  box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
}

/* EMPTY STATE */
.empty-results {
  text-align: center;
  padding: 60px 20px;
  background: var(--os-surface);
  border: 1px dashed var(--os-border);
  border-radius: var(--os-radius-lg);
  display: none;
}

.empty-results i {
  font-size: 3rem;
  color: var(--os-cyan-bright);
  margin-bottom: 16px;
}

/* TOAST NOTIFICATION */
.osint-toast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #0f172a;
  border: 1px solid var(--os-cyan-bright);
  color: #ffffff;
  padding: 12px 22px;
  border-radius: var(--os-radius-md);
  font-size: 0.9rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 1000;
  transform: translateY(100px);
  opacity: 0;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.osint-toast.visible {
  transform: translateY(0);
  opacity: 1;
}

/* SEO KNOWLEDGE & FAQ SECTION */
.seo-knowledge-section {
  background: var(--os-surface);
  border: 1px solid var(--os-border);
  border-radius: var(--os-radius-lg);
  padding: 40px;
  margin-top: 50px;
  box-shadow: var(--os-shadow);
}

.seo-knowledge-section h2 {
  font-size: 1.8rem;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 20px;
  border-bottom: 2px solid var(--os-border);
  padding-bottom: 12px;
}

body.daylight-lab .seo-knowledge-section h2 {
  color: #0f172a;
}

.seo-knowledge-section h3 {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--os-cyan-bright);
  margin: 28px 0 14px;
}

.seo-knowledge-section p, .seo-knowledge-section li {
  color: var(--os-text-muted);
  font-size: 0.95rem;
  line-height: 1.7;
}

.framework-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  margin: 24px 0;
}

.framework-card {
  background: var(--os-card);
  border: 1px solid var(--os-border);
  border-radius: var(--os-radius-md);
  padding: 20px;
}

.framework-num {
  font-size: 1.8rem;
  font-weight: 800;
  font-family: var(--os-font-mono);
  color: var(--os-cyan-bright);
  margin-bottom: 8px;
}

.framework-card h4 {
  font-size: 1.05rem;
  color: #ffffff;
  margin-bottom: 8px;
}

body.daylight-lab .framework-card h4 {
  color: #0f172a;
}

/* FAQ ACCORDION */
.faq-grid {
  margin-top: 24px;
}

.faq-item {
  background: var(--os-card);
  border: 1px solid var(--os-border);
  border-radius: var(--os-radius-md);
  margin-bottom: 14px;
  overflow: hidden;
}

.faq-question {
  padding: 18px 22px;
  font-weight: 700;
  font-size: 1.05rem;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #ffffff;
}

body.daylight-lab .faq-question {
  color: #0f172a;
}

.faq-question i {
  color: var(--os-cyan-bright);
  transition: transform 0.3s;
}

.faq-item.active .faq-question i {
  transform: rotate(180deg);
}

.faq-answer {
  padding: 0 22px 18px;
  color: var(--os-text-muted);
  line-height: 1.6;
  display: none;
}

.faq-item.active .faq-answer {
  display: block;
}

/* SEMANTIC CRAWLABLE CATEGORIES INDEX */
.seo-crawler-index {
  margin-top: 36px;
  padding-top: 28px;
  border-top: 1px solid var(--os-border);
}

.seo-crawler-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 16px;
}

.seo-cat-block h4 {
  color: var(--os-cyan-bright);
  font-size: 0.95rem;
  margin-bottom: 8px;
}

.seo-cat-block ul {
  list-style: none;
  padding-left: 0;
}

.seo-cat-block li {
  font-size: 0.82rem;
  margin-bottom: 6px;
}

.seo-cat-block a {
  color: var(--os-text);
  text-decoration: underline;
}

.share-banner {
  margin-top: 40px;
  padding: 24px;
  background: linear-gradient(135deg, rgba(6, 182, 212, 0.1), rgba(139, 92, 246, 0.1));
  border: 1px solid var(--os-border-glow);
  border-radius: var(--os-radius-md);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}

.share-btns {
  display: flex;
  gap: 10px;
}

.share-btn {
  padding: 10px 16px;
  border-radius: 8px;
  color: #fff;
  font-size: 0.85rem;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.share-x { background: #000000; border: 1px solid #333; }
.share-li { background: #0a66c2; }
.share-rd { background: #ff4500; }

/* RESPONSIVE */
@media (max-width: 768px) {
  .osint-wrapper {
    padding: 20px 10px 60px;
  }
  .osint-toolbar {
    padding: 14px;
    top: 5px;
  }
  .toolbar-primary {
    flex-direction: column;
    align-items: stretch;
  }
  .toolbar-controls {
    justify-content: space-between;
  }
  .tools-grid-container {
    grid-template-columns: 1fr;
  }
  .tools-grid-container.list-mode .osint-card {
    flex-direction: column;
    align-items: stretch;
  }
  .tools-grid-container.list-mode .card-top,
  .tools-grid-container.list-mode .card-actions {
    width: 100%;
  }
  .seo-knowledge-section {
    padding: 20px;
  }
}
</style>

<div class="osint-wrapper" id="osint-app">
  <div class="osint-container">
    
    <!-- ==================== HERO SECTION ==================== -->
    <header class="osint-hero">
      <div class="osint-hero-badge">
        <span class="live-pulse"></span> VERIFIED OSINT DIRECTORY // 2026 EDITION
      </div>
      <h1>The Ultimate OSINT Toolkit & Intelligence Suite</h1>
      <p class="osint-hero-lead">
        Access <strong>1,450+ hand-curated Open Source Intelligence tools</strong>, darknet research directories, SOCMINT social trackers, threat intel feeds, and OpSec sandboxes. Built for cyber analysts, investigative journalists, and security professionals.
      </p>

      <!-- KPI STATS -->
      <div class="osint-stats-row">
        <div class="kpi-pill">
          <span class="kpi-num">1,456</span>
          <span class="kpi-lbl">Verified Tools</span>
        </div>
        <div class="kpi-pill">
          <span class="kpi-num">79</span>
          <span class="kpi-lbl">Categories</span>
        </div>
        <div class="kpi-pill">
          <span class="kpi-num">10</span>
          <span class="kpi-lbl">Core Domains</span>
        </div>
        <div class="kpi-pill">
          <span class="kpi-num">100%</span>
          <span class="kpi-lbl">Free Access</span>
        </div>
      </div>
    </header>

    <!-- ==================== RECON QUICK PIVOT CONSOLE ==================== -->
    <section class="recon-console" aria-label="Target Quick Pivot Console">
      <div class="recon-console-header">
        <div class="recon-title">
          <i class="fas fa-crosshairs"></i> Universal Quick-Pivot Target Launcher
        </div>
        <span class="recon-badge">One-Click Deep Recon</span>
      </div>
      <div class="recon-input-wrap">
        <input type="text" id="recon-target" class="recon-target-input" placeholder="Enter target username, domain, email, IP, or hash (e.g. john_doe, github.com)..." aria-label="Investigation Target">
      </div>
      <div class="recon-buttons">
        <button class="pivot-btn" onclick="launchPivot('dork')"><i class="fab fa-google"></i> Google Dorks</button>
        <button class="pivot-btn" onclick="launchPivot('shodan')"><i class="fas fa-network-wired"></i> Shodan</button>
        <button class="pivot-btn" onclick="launchPivot('virustotal')"><i class="fas fa-shield-virus"></i> VirusTotal</button>
        <button class="pivot-btn" onclick="launchPivot('wayback')"><i class="fas fa-history"></i> Wayback Archive</button>
        <button class="pivot-btn" onclick="launchPivot('whatsmyname')"><i class="fas fa-user-tag"></i> WhatsMyName</button>
        <button class="pivot-btn" onclick="launchPivot('epieos')"><i class="fas fa-envelope-open-text"></i> Epieos Email</button>
        <button class="pivot-btn" onclick="launchPivot('cyberchef')"><i class="fas fa-hat-wizard"></i> CyberChef</button>
        <button class="pivot-btn" onclick="launchPivot('whois')"><i class="fas fa-id-badge"></i> Whois Lookup</button>
      </div>
    </section>

    <!-- ==================== INTERACTIVE TOOLBAR ==================== -->
    <section class="osint-toolbar" aria-label="Search and Filter Toolbar">
      <!-- Search Input & Global Controls -->
      <div class="toolbar-primary">
        <div class="search-container">
          <i class="fas fa-search search-icon"></i>
          <input type="text" id="osint-search" class="osint-search-input" placeholder="Search 1,456 tools by name, description, category, or URL (e.g. twitter, reverse image, shodan, whois)..." autocomplete="off" spellcheck="false">
          <button id="clear-search" class="clear-search-btn" title="Clear search"><i class="fas fa-times"></i></button>
        </div>

        <div class="toolbar-controls">
          <!-- Subcategory Dropdown -->
          <div class="select-wrap">
            <select id="subcat-select" aria-label="Filter by Subcategory">
              <option value="ALL">All Categories (79)</option>
              <option value="ANALYTICS">ANALYTICS (10)</option>
<option value="BLOG">BLOG (4)</option>
<option value="BOT">BOT (5)</option>
<option value="BUSINESS">BUSINESS (27)</option>
<option value="CLUBHOUSE">CLUBHOUSE (3)</option>
<option value="CRYPTOCURRENCY">CRYPTOCURRENCY (11)</option>
<option value="DARKNET">DARKNET (15)</option>
<option value="DATA DUMP">DATA DUMP (16)</option>
<option value="DATASET">DATASET (14)</option>
<option value="DISCORD">DISCORD (13)</option>
<option value="DOMAIN / IP / DNS">DOMAIN / IP / DNS (53)</option>
<option value="DORKING">DORKING (8)</option>
<option value="DOWNLOADER">DOWNLOADER (9)</option>
<option value="EMAIL">EMAIL (26)</option>
<option value="EXTREMIST / FAR-RIGHT">EXTREMIST / FAR-RIGHT (24)</option>
<option value="FACEBOOK">FACEBOOK (16)</option>
<option value="FILE UPLOAD">FILE UPLOAD (6)</option>
<option value="FINANCE">FINANCE (9)</option>
<option value="FLIGHT TRACKER">FLIGHT TRACKER (10)</option>
<option value="GEO">GEO (18)</option>
<option value="GOOGLE">GOOGLE (4)</option>
<option value="GOOGLE CSE">GOOGLE CSE (19)</option>
<option value="GOVERNMENT">GOVERNMENT (48)</option>
<option value="HASH RECOVERY">HASH RECOVERY (8)</option>
<option value="ID GENERATOR">ID GENERATOR (33)</option>
<option value="IDENTITY RESOLUTION">IDENTITY RESOLUTION (3)</option>
<option value="IMAGE / VIDEO / AUDIO / MEDIA">IMAGE / VIDEO / AUDIO / MEDIA (41)</option>
<option value="INFORMANT">INFORMANT (3)</option>
<option value="INSTAGRAM">INSTAGRAM (19)</option>
<option value="IoT">IoT (30)</option>
<option value="LICENSE PLATE / VIN / VEHICLE">LICENSE PLATE / VIN / VEHICLE (30)</option>
<option value="LINKEDIN">LINKEDIN (9)</option>
<option value="MALWARE">MALWARE (15)</option>
<option value="MAPS">MAPS (47)</option>
<option value="MARITIME">MARITIME (19)</option>
<option value="MASTODON">MASTODON (2)</option>
<option value="NEWS">NEWS (23)</option>
<option value="ONLYFANS">ONLYFANS (6)</option>
<option value="OPEN DIRECTORY">OPEN DIRECTORY (23)</option>
<option value="OTHER">OTHER (2)</option>
<option value="PEOPLE">PEOPLE (26)</option>
<option value="PHONE">PHONE (27)</option>
<option value="POLICE / LE / FED">POLICE / LE / FED (43)</option>
<option value="PRIVACY / SECURITY">PRIVACY / SECURITY (22)</option>
<option value="PRODUCTIVITY">PRODUCTIVITY (57)</option>
<option value="PUBLIC RECORDS">PUBLIC RECORDS (46)</option>
<option value="RADIO">RADIO (18)</option>
<option value="REAL ESTATE">REAL ESTATE (10)</option>
<option value="REDDIT">REDDIT (34)</option>
<option value="RESIDENT DATABASE">RESIDENT DATABASE (5)</option>
<option value="RESOLVERS">RESOLVERS (6)</option>
<option value="RESOURCES">RESOURCES (54)</option>
<option value="SANDBOX / EMULATOR">SANDBOX / EMULATOR (7)</option>
<option value="SEARCH ENGINES">SEARCH ENGINES (70)</option>
<option value="SECURE COMMUNICATION">SECURE COMMUNICATION (20)</option>
<option value="SEX OFFENDER">SEX OFFENDER (11)</option>
<option value="SNAPCHAT">SNAPCHAT (7)</option>
<option value="SOCIAL MEDIA">SOCIAL MEDIA (15)</option>
<option value="SOURCE CODES">SOURCE CODES (21)</option>
<option value="STEAM">STEAM (3)</option>
<option value="TELEGRAM">TELEGRAM (16)</option>
<option value="THREAT INTEL">THREAT INTEL (17)</option>
<option value="THROWAWAY CONTACT">THROWAWAY CONTACT (18)</option>
<option value="TIKTOK">TIKTOK (4)</option>
<option value="TOOLSET">TOOLSET (37)</option>
<option value="TWITCH">TWITCH (13)</option>
<option value="TWITTER">TWITTER (40)</option>
<option value="UNIFIED SEARCH">UNIFIED SEARCH (13)</option>
<option value="USERNAME">USERNAME (19)</option>
<option value="VOTER DATABASES">VOTER DATABASES (17)</option>
<option value="WEATHER">WEATHER (4)</option>
<option value="WHOIS">WHOIS (5)</option>
<option value="YOUTUBE">YOUTUBE (17)</option>
<option value="[CAN] CORPORATION">[CAN] CORPORATION (21)</option>
<option value="[CAN] GOVERNMENT">[CAN] GOVERNMENT (23)</option>
<option value="[CAN] IOT">[CAN] IOT (5)</option>
<option value="[CAN] POLICE">[CAN] POLICE (4)</option>
            </select>
          </div>

          <!-- Sort Order -->
          <div class="select-wrap">
            <select id="sort-select" aria-label="Sort Tools">
              <option value="default">Sort: Recommended</option>
              <option value="az">Sort: Alphabetical (A-Z)</option>
              <option value="za">Sort: Alphabetical (Z-A)</option>
              <option value="cat">Sort: By Category</option>
            </select>
          </div>

          <!-- View Mode Toggle -->
          <button id="view-grid" class="btn-icon-toggle active" title="Grid View" aria-label="Grid View"><i class="fas fa-th-large"></i></button>
          <button id="view-list" class="btn-icon-toggle" title="List View" aria-label="List View"><i class="fas fa-list"></i></button>

          <!-- Day / Night Theme Toggle -->
          <button id="theme-toggle" class="btn-icon-toggle" title="Toggle Day/Night Theme" aria-label="Toggle Theme"><i class="fas fa-sun"></i></button>

          <!-- Action Buttons -->
          <button class="btn-action btn-random" onclick="pickRandomTool()" title="Discover Random Tool"><i class="fas fa-dice"></i> Random Tool</button>
          <button class="btn-action" onclick="exportBookmarksHTML()" title="Export all tools to browser bookmarks"><i class="fas fa-file-export"></i> Export HTML</button>
          <button class="btn-action" onclick="exportJSON()" title="Export tools as JSON"><i class="fas fa-code"></i> JSON</button>
        </div>
      </div>

      <!-- Domain Group Pills -->
      <div class="domain-tabs-scroll" id="domain-tabs" role="tablist">
        <button class="domain-tab active" data-group="ALL">All Tools <span class="domain-tab-count">1456</span></button>
        <button class="domain-tab" data-group="FAVORITES">★ Favorites <span class="domain-tab-count" id="fav-count">0</span></button>
        <button class="domain-tab" data-group="People & Identity">People & Identity <span class="domain-tab-count">163</span></button>
        <button class="domain-tab" data-group="Social Media (SOCMINT)">Social Media <span class="domain-tab-count">222</span></button>
        <button class="domain-tab" data-group="Search & Dorking">Search & Dorking <span class="domain-tab-count">152</span></button>
        <button class="domain-tab" data-group="Domain, IP & Threat Intel">Domain & Threat Intel <span class="domain-tab-count">133</span></button>
        <button class="domain-tab" data-group="Maps & GEOINT">Maps & GEOINT <span class="domain-tab-count">126</span></button>
        <button class="domain-tab" data-group="Public Records & Gov">Public Records <span class="domain-tab-count">240</span></button>
        <button class="domain-tab" data-group="Finance & Business">Finance & Business <span class="domain-tab-count">77</span></button>
        <button class="domain-tab" data-group="Media Forensics & Data">Media & Forensics <span class="domain-tab-count">101</span></button>
        <button class="domain-tab" data-group="OpSec & Secure Comms">OpSec & Privacy <span class="domain-tab-count">55</span></button>
        <button class="domain-tab" data-group="Toolsets & Productivity">Toolsets & Utilities <span class="domain-tab-count">187</span></button>
      </div>

      <!-- Live Results Meta Bar -->
      <div class="results-meta-bar">
        <span class="results-count" id="results-count">Showing <strong>1,456</strong> of <strong>1,456</strong> tools</span>
        <span class="results-tag" id="current-scope">Scope: All Domains</span>
      </div>
    </section>

    <!-- ==================== TOOLS GRID CONTAINER ==================== -->
    <div id="tools-container" class="tools-grid-container" role="feed" aria-busy="false">
      <!-- Dynamically populated via JS -->
    </div>

    <!-- Empty Search State -->
    <div id="empty-state" class="empty-results">
      <i class="fas fa-radar"></i>
      <h3>No matching investigative tools found</h3>
      <p>Try searching for a broader keyword (e.g., "phone", "email", "image", "dns") or reset filters.</p>
      <button class="btn-action" onclick="resetAllFilters()" style="margin-top:16px;"><i class="fas fa-redo"></i> Reset All Filters</button>
    </div>

    <!-- Load More Section -->
    <div class="load-more-section" id="load-more-wrap">
      <button id="btn-load-more" class="btn-load-more" onclick="renderMoreTools()">
        <i class="fas fa-plus-circle"></i> Load More Tools (<span id="load-more-remaining">0</span> remaining)
      </button>
      <button class="btn-action" onclick="loadAllTools()" style="margin-left:12px;" title="Render all tools immediately">
        Show All
      </button>
    </div>

    <!-- ==================== TOAST NOTIFICATION ==================== -->
    <div id="osint-toast" class="osint-toast" role="status">
      <i class="fas fa-check-circle" style="color:var(--os-emerald);"></i>
      <span id="toast-msg">Tool link copied to clipboard!</span>
    </div>

    <!-- ==================== VIRAL SEO KNOWLEDGE BASE & PLAYBOOK ==================== -->
    <article class="seo-knowledge-section">
      <h2>The Complete OSINT Investigation Framework & Methodology (2026 Guide)</h2>
      <p>
        Open Source Intelligence (OSINT) is the disciplined practice of collecting, processing, and analyzing publicly available data to produce actionable intelligence. Whether you are conducting corporate due diligence, verifying human rights reporting, investigating cyber fraud, or performing threat hunting, a structured methodology separates amateur browsing from professional intelligence tradecraft.
      </p>

      <h3>The 5 Phases of the Professional Intelligence Cycle</h3>
      <div class="framework-grid">
        <div class="framework-card">
          <div class="framework-num">01</div>
          <h4>Direction & Planning</h4>
          <p>Define clear Priority Intelligence Requirements (PIRs). Establish scope, identify target indicators (selectors), and define legal and jurisdictional boundaries before executing queries.</p>
        </div>
        <div class="framework-card">
          <div class="framework-num">02</div>
          <h4>Passive Collection</h4>
          <p>Harvest public records, social media handles, DNS history, and archived web pages without sending direct network packets to the subject’s infrastructure to avoid detection.</p>
        </div>
        <div class="framework-card">
          <div class="framework-num">03</div>
          <h4>Processing & Normalization</h4>
          <p>Extract EXIF metadata, decode obfuscated strings in CyberChef, cross-reference usernames, geolocate IP allocations, and clean tabular CSV datasets into unified timelines.</p>
        </div>
        <div class="framework-card">
          <div class="framework-num">04</div>
          <h4>Correlation & Analysis</h4>
          <p>Connect disparate entities through link analysis. Verify findings using at least two independent primary sources to eliminate disinformation or synthetic sock puppets.</p>
        </div>
        <div class="framework-card">
          <div class="framework-num">05</div>
          <h4>Dissemination & Archival</h4>
          <p>Preserve evidentiary web snapshots via Wayback Machine or Archive.is, compile verified chronologies, and produce clear, verifiable intelligence briefings.</p>
        </div>
      </div>

      <h3>Essential OpSec (Operational Security) Rules for Investigators</h3>
      <ul>
        <li><strong>Isolate Research Workstations:</strong> Never investigate high-risk entities from your personal browser. Use containerized browsers (such as <em>Kasm Web</em>), disposable Virtual Machines, or separate hardened operating systems (such as Tails or Whonix).</li>
        <li><strong>Maintain Clean Sock Puppets:</strong> When creating research accounts on social media, use synthetic persona generators (Fake Name Generator, This Person Does Not Exist) and burner phone numbers (OnlineSim, SMS To Me) to prevent attribution back to your real identity.</li>
        <li><strong>Disable WebRTC and Leaks:</strong> Ensure your investigative browser blocks WebRTC IP leaks, disables automatic image loading if investigating hostile domains, and routes through reputable VPNs or Tor circuits.</li>
        <li><strong>Timely Evidence Preservation:</strong> Suspects frequently delete posts, alter bios, or take down websites once alerted. Immediately preserve target pages using <em>Archive.is</em> and <em>Wayback Machine</em> with cryptographic hashes.</li>
      </ul>

      <h3>Top 10 High-Impact Google Search Operators (Dorks)</h3>
      <p>Mastering Google search operators is the bedrock of targeted intelligence gathering:</p>
      <ul>
        <li><code>site:target.com filetype:pdf confidential</code> — Finds sensitive indexed PDF documents.</li>
        <li><code>site:target.com inurl:admin | inurl:login</code> — Discovers exposed administrative portals.</li>
        <li><code>"target username" site:github.com | site:pastebin.com</code> — Identifies leaked credentials or source code repositories.</li>
        <li><code>site:linkedin.com/in/ "Target Company" "Former"</code> — Maps past employees who may hold operational insights.</li>
        <li><code>intitle:"index of" "parent directory" (passwd | credentials | dump)</code> — Detects misconfigured open HTTP/FTP directories.</li>
      </ul>

      <!-- FAQ ACCORDION -->
      <h3>Frequently Asked Questions (FAQ)</h3>
      <div class="faq-grid">
        <div class="faq-item">
          <div class="faq-question">
            <span>What is the difference between Active and Passive Reconnaissance?</span>
            <i class="fas fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p><strong>Passive Reconnaissance</strong> gathers information without directly interacting with the target's servers or infrastructure (e.g., querying cached Google records, WHOIS databases, or Shodan historical data). The target has no log record of your investigation. <strong>Active Reconnaissance</strong> sends packets directly to the target (e.g., port scanning with Nmap or crawling an active web server), which will generate logs and alert security systems.</p>
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            <span>How can I reverse search a username across hundreds of social networks?</span>
            <i class="fas fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p>Use automated tools like <em>WhatsMyName</em>, <em>Sherlock</em>, or <em>Namechk</em>. These tools test HTTP response codes across over 500 platforms to check if a specific username exists, allowing you to map an individual's digital footprint across niche forums, developer platforms, and mainstream networks.</p>
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            <span>What are the legal boundaries of OSINT research?</span>
            <i class="fas fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p>OSINT operates strictly within legal parameters by analyzing data that is intentionally published or made publicly accessible. Bypassing authentication, cracking passwords, exploiting vulnerabilities, or circumventing paywalls through unauthorized network access crosses the line into computer crimes (such as the CFAA in the United States or GDPR breaches in Europe).</p>
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            <span>Can I export this entire tool directory to my browser bookmarks?</span>
            <i class="fas fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p>Yes! Click the <strong>Export HTML</strong> button on the toolbar above. This generates a standardized Netscape Bookmark file organized by category that can be imported directly into Google Chrome, Brave, Mozilla Firefox, Microsoft Edge, and Safari in under 5 seconds.</p>
          </div>
        </div>
      </div>

      <!-- SEMANTIC CRAWLABLE CATEGORIES INDEX -->
      <div class="seo-crawler-index">
        <h3>Index of Key Intelligence Directories</h3>
        <p>Explore verified resources across key disciplines:</p>
        <div class="seo-crawler-grid">
          
    <div class="seo-cat-block">
      <h4>SEARCH ENGINES <span class="badge">(70 tools)</span></h4>
      <ul><li><a href="https://inteltechniques.com/tools/Search.html" target="_blank" rel="noopener noreferrer">IntelTechniques Search Engine</a>: <span>Michael Bazzell premier OSINT investigation methodology, training, and custom search engines.</span></li><li><a href="https://www.google.com/advanced_search" target="_blank" rel="noopener noreferrer">Google Advanced Search</a>: <span>Alternative, privacy-respecting, or regional search engine offering specialized indexing.</span></li><li><a href="https://searx.info/" target="_blank" rel="noopener noreferrer">Searx</a>: <span>Alternative, privacy-respecting, or regional search engine offering specialized indexing.</span></li><li><a href="https://www.bing.com/" target="_blank" rel="noopener noreferrer">Bing</a>: <span>Alternative, privacy-respecting, or regional search engine offering specialized indexing.</span></li><li><a href="https://yandex.com/" target="_blank" rel="noopener noreferrer">Yandex</a>: <span>Alternative, privacy-respecting, or regional search engine offering specialized indexing.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>PRODUCTIVITY <span class="badge">(57 tools)</span></h4>
      <ul><li><a href="https://dfir.blog/unfurl/" target="_blank" rel="noopener noreferrer">unfurl</a>: <span>Investigative utility for data transformation, evidence transcription, and case documentation.</span></li><li><a href="https://www.wolframalpha.com/" target="_blank" rel="noopener noreferrer">Wolfram|Alpha</a>: <span>Computational knowledge engine for computing data, answering factual queries, and deep analysis.</span></li><li><a href="https://cryptpad.fr/" target="_blank" rel="noopener noreferrer">Cryptpad.fr</a>: <span>Investigative utility for data transformation, evidence transcription, and case documentation.</span></li><li><a href="https://recontool.org/" target="_blank" rel="noopener noreferrer">Recontool.org</a>: <span>Investigative utility for data transformation, evidence transcription, and case documentation.</span></li><li><a href="https://app.mindmup.com/map/new" target="_blank" rel="noopener noreferrer">MindMup 2</a>: <span>Investigative utility for data transformation, evidence transcription, and case documentation.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>RESOURCES <span class="badge">(54 tools)</span></h4>
      <ul><li><a href="https://ohshint.gitbook.io/" target="_blank" rel="noopener noreferrer">OH SHINT! Welcome Aboard</a>: <span>Authoritative OSINT cheatsheet, methodology guide, framework documentation, or bookmark index.</span></li><li><a href="https://start.me/p/DPYPMz/the-ultimate-osint-collection" target="_blank" rel="noopener noreferrer">The Ultimate OSINT Collection</a>: <span>Authoritative OSINT cheatsheet, methodology guide, framework documentation, or bookmark index.</span></li><li><a href="https://start.me/p/aLe0vp/osint-resources-in-canada" target="_blank" rel="noopener noreferrer">OSINT Resources in Canada</a>: <span>Authoritative OSINT cheatsheet, methodology guide, framework documentation, or bookmark index.</span></li><li><a href="https://start.me/p/rx6Qj8/nixintel-s-osint-resource-list" target="_blank" rel="noopener noreferrer">Nixintel&#x27;s OSINT Resource List</a>: <span>Authoritative OSINT cheatsheet, methodology guide, framework documentation, or bookmark index.</span></li><li><a href="https://start.me/p/1kvvxN/faros-osint-resources" target="_blank" rel="noopener noreferrer">FAROS OSINT Resources</a>: <span>Authoritative OSINT cheatsheet, methodology guide, framework documentation, or bookmark index.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>DOMAIN / IP / DNS <span class="badge">(53 tools)</span></h4>
      <ul><li><a href="https://domainbigdata.com/" target="_blank" rel="noopener noreferrer">domainbigdata</a>: <span>DNS analyzer, reverse IP lookup, subnet scanner, and passive DNS database.</span></li><li><a href="https://www.domaincodex.com/search.php" target="_blank" rel="noopener noreferrer">Domain Codex</a>: <span>DNS analyzer, reverse IP lookup, subnet scanner, and passive DNS database.</span></li><li><a href="https://dnslytics.com/" target="_blank" rel="noopener noreferrer">dnslytics</a>: <span>DNS analyzer, reverse IP lookup, subnet scanner, and passive DNS database.</span></li><li><a href="https://securitytrails.com/" target="_blank" rel="noopener noreferrer">SecurityTrails</a>: <span>DNS analyzer, reverse IP lookup, subnet scanner, and passive DNS database.</span></li><li><a href="https://shodan.io" target="_blank" rel="noopener noreferrer">Shodan</a>: <span>Search engine for Internet-connected devices, industrial control systems, cameras, and open ports.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>GOVERNMENT <span class="badge">(48 tools)</span></h4>
      <ul><li><a href="https://data.occrp.org/" target="_blank" rel="noopener noreferrer">data.occrp.org</a>: <span>Official government portal, state registry, FOIA request tracker, and legislative repository.</span></li><li><a href="https://cdn.occrp.org/projects/project-p/#/" target="_blank" rel="noopener noreferrer">The Pegasus Project | OCCRP</a>: <span>Official government portal, state registry, FOIA request tracker, and legislative repository.</span></li><li><a href="https://datawrapper.dwcdn.net/UCUWs/3/" target="_blank" rel="noopener noreferrer">COP26 registered attendees</a>: <span>Official government portal, state registry, FOIA request tracker, and legislative repository.</span></li><li><a href="https://www.muckrock.com/" target="_blank" rel="noopener noreferrer">MuckRock</a>: <span>Official government portal, state registry, FOIA request tracker, and legislative repository.</span></li><li><a href="https://govsalaries.com/" target="_blank" rel="noopener noreferrer">GovSalaries</a>: <span>Official government portal, state registry, FOIA request tracker, and legislative repository.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>MAPS <span class="badge">(47 tools)</span></h4>
      <ul><li><a href="https://www.google.com/maps" target="_blank" rel="noopener noreferrer">Google Maps</a>: <span>Interactive satellite imagery, topographic maps, street view archives, and geospatial overlays.</span></li><li><a href="https://www.bing.com/maps" target="_blank" rel="noopener noreferrer">Bing Maps</a>: <span>Interactive satellite imagery, topographic maps, street view archives, and geospatial overlays.</span></li><li><a href="https://yandex.com/maps/" target="_blank" rel="noopener noreferrer">Yandex.Maps</a>: <span>Interactive satellite imagery, topographic maps, street view archives, and geospatial overlays.</span></li><li><a href="https://www.udeuschle.de/panoramas/makepanoramas_en.htm" target="_blank" rel="noopener noreferrer">Generate a panorama</a>: <span>Interactive satellite imagery, topographic maps, street view archives, and geospatial overlays.</span></li><li><a href="https://www.mapillary.com/app/" target="_blank" rel="noopener noreferrer">Mapillary</a>: <span>Interactive satellite imagery, topographic maps, street view archives, and geospatial overlays.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>PUBLIC RECORDS <span class="badge">(46 tools)</span></h4>
      <ul><li><a href="https://www.judyrecords.com/" target="_blank" rel="noopener noreferrer">JudyRecords</a>: <span>Public records aggregator for vital statistics, court filings, property deeds, and bankruptcies.</span></li><li><a href="https://www.courtlistener.com/" target="_blank" rel="noopener noreferrer">CourtListener</a>: <span>Public records aggregator for vital statistics, court filings, property deeds, and bankruptcies.</span></li><li><a href="https://pacer.uscourts.gov/" target="_blank" rel="noopener noreferrer">Public Access to Court Electronic Records</a>: <span>Public records aggregator for vital statistics, court filings, property deeds, and bankruptcies.</span></li><li><a href="https://parallelsearch.casetext.com/" target="_blank" rel="noopener noreferrer">Parallelsearch case law</a>: <span>Public records aggregator for vital statistics, court filings, property deeds, and bankruptcies.</span></li><li><a href="https://www.canlii.org/en/" target="_blank" rel="noopener noreferrer">Canadian Legal Information Institute</a>: <span>Public records aggregator for vital statistics, court filings, property deeds, and bankruptcies.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>POLICE / LE / FED <span class="badge">(43 tools)</span></h4>
      <ul><li><a href="https://openoversight.com/" target="_blank" rel="noopener noreferrer">Openoversight</a>: <span>Law enforcement intelligence tool, criminal history search, inmate locator, and police blotters.</span></li><li><a href="https://extras.mercurynews.com/criminalcops/database/" target="_blank" rel="noopener noreferrer">Criminal Cop Database Lookup</a>: <span>Law enforcement intelligence tool, criminal history search, inmate locator, and police blotters.</span></li><li><a href="https://datawrapper.dwcdn.net/3GbVI/1/" target="_blank" rel="noopener noreferrer">The Philadelphia Police Misconduct Database</a>: <span>Law enforcement intelligence tool, criminal history search, inmate locator, and police blotters.</span></li><li><a href="https://nyclu.shinyapps.io/CCRB_combo/" target="_blank" rel="noopener noreferrer">NYPD Misconduct Complaint Database</a>: <span>Law enforcement intelligence tool, criminal history search, inmate locator, and police blotters.</span></li><li><a href="https://nypdonline.org/link/2" target="_blank" rel="noopener noreferrer">NYPD Officer Profile</a>: <span>Law enforcement intelligence tool, criminal history search, inmate locator, and police blotters.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>IMAGE / VIDEO / AUDIO / MEDIA <span class="badge">(41 tools)</span></h4>
      <ul><li><a href="https://facecheck.id/" target="_blank" rel="noopener noreferrer">Facecheck.id</a>: <span>Forensic media tool for EXIF metadata extraction, reverse image search, or face matching.</span></li><li><a href="https://images.google.com/" target="_blank" rel="noopener noreferrer">Google Images</a>: <span>Forensic media tool for EXIF metadata extraction, reverse image search, or face matching.</span></li><li><a href="https://yandex.com/images/" target="_blank" rel="noopener noreferrer">Yandex Images</a>: <span>Forensic media tool for EXIF metadata extraction, reverse image search, or face matching.</span></li><li><a href="https://www.bing.com/images" target="_blank" rel="noopener noreferrer">Bing Images</a>: <span>Forensic media tool for EXIF metadata extraction, reverse image search, or face matching.</span></li><li><a href="https://www.bing.com/visualsearch" target="_blank" rel="noopener noreferrer">See it, search it</a>: <span>Search the web using an image instead of text. Reverse image search engine. Search by image: Take a picture or upload one to find similar images and products. Identify landmarks, animals, even cele...</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>TWITTER <span class="badge">(40 tools)</span></h4>
      <ul><li><a href="https://inteltechniques.com/tools/Twitter.html" target="_blank" rel="noopener noreferrer">IntelTechniques Twitter</a>: <span>Michael Bazzell premier OSINT investigation methodology, training, and custom search engines.</span></li><li><a href="https://nitter.hu" target="_blank" rel="noopener noreferrer">Nitter.hu</a>: <span>X (Twitter) investigative tool for scraping tweets, follower graphs, and bot activity analysis.</span></li><li><a href="https://nitter.it" target="_blank" rel="noopener noreferrer">Nitter.it</a>: <span>X (Twitter) investigative tool for scraping tweets, follower graphs, and bot activity analysis.</span></li><li><a href="https://birdhunt.co/" target="_blank" rel="noopener noreferrer">BirdHunt</a>: <span>X (Twitter) investigative tool for scraping tweets, follower graphs, and bot activity analysis.</span></li><li><a href="https://xnaas.github.io/nitter-instances/" target="_blank" rel="noopener noreferrer">Nitter Instances</a>: <span>X (Twitter) investigative tool for scraping tweets, follower graphs, and bot activity analysis.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>TOOLSET <span class="badge">(37 tools)</span></h4>
      <ul><li><a href="https://gchq.github.io/CyberChef/" target="_blank" rel="noopener noreferrer">CyberChef</a>: <span>The Cyber Swiss Army Knife for encryption, decoding, hex analysis, data format conversion, and hashing.</span></li><li><a href="https://github.com/ninoseki/mitaka" target="_blank" rel="noopener noreferrer">mitaka</a>: <span>Comprehensive reconnaissance suite, multi-tool aggregator, or specialized investigative script.</span></li><li><a href="https://github.com/sensepost/Frack" target="_blank" rel="noopener noreferrer">Frack</a>: <span>Frack is my attempt at creating an end-to-end solution to store, manage and query your breach data. The tool has got a very basic workflow making it easy to use.</span></li><li><a href="https://pypi.org/project/pywhat/" target="_blank" rel="noopener noreferrer">pywhat</a>: <span>Comprehensive reconnaissance suite, multi-tool aggregator, or specialized investigative script.</span></li><li><a href="https://pypi.org/project/theHarvester/" target="_blank" rel="noopener noreferrer">theHarvester</a>: <span>theHarvester is a very simple, yet effective tool designed to be used in the early
stages of a penetration test. Use it for open source intelligence gathering and helping
to determine a company&#x27;s external threat landscape on the internet</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>REDDIT <span class="badge">(34 tools)</span></h4>
      <ul><li><a href="https://teddit.net/" target="_blank" rel="noopener noreferrer">teddit</a>: <span>Reddit privacy frontend</span></li><li><a href="https://camas.unddit.com/" target="_blank" rel="noopener noreferrer">Reddit Search</a>: <span>Search reddit using the pushshift.io API. For more advanced searches you can directly query the API fairly easily.</span></li><li><a href="http://karmadecay.com/" target="_blank" rel="noopener noreferrer">Karma Decay</a>: <span>Reddit investigative tool for analyzing user comment histories and tracking deleted posts.</span></li><li><a href="https://pypi.org/project/redditsfinder/" target="_blank" rel="noopener noreferrer">redditsfinder</a>: <span>A command line program to easily download reddit users&#x27; post histories.</span></li><li><a href="https://www.socialgrep.com/search" target="_blank" rel="noopener noreferrer">SocialGrep</a>: <span>Social media statistics for Reddit - popular communities, trending topics, and more</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>ID GENERATOR <span class="badge">(33 tools)</span></h4>
      <ul><li><a href="https://www.lastpass.com/features/username-generator" target="_blank" rel="noopener noreferrer">Username Generator</a>: <span>Synthetic persona generator for realistic dummy profiles and non-attributable sock puppets.</span></li><li><a href="https://www.fakenamegenerator.com/" target="_blank" rel="noopener noreferrer">Fake Name Generator</a>: <span>Generates comprehensive fictitious identities with address, SSN, credit card, and employment.</span></li><li><a href="https://thisresumedoesnotexist.com/" target="_blank" rel="noopener noreferrer">Resume Generator</a>: <span>Synthetic persona generator for realistic dummy profiles and non-attributable sock puppets.</span></li><li><a href="https://www.behindthename.com/random/" target="_blank" rel="noopener noreferrer">International Name Generator</a>: <span>Synthetic persona generator for realistic dummy profiles and non-attributable sock puppets.</span></li><li><a href="https://wpimeigenerator.github.io/" target="_blank" rel="noopener noreferrer">Windows Phone IMEI Generator</a>: <span>Synthetic persona generator for realistic dummy profiles and non-attributable sock puppets.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>LICENSE PLATE / VIN / VEHICLE <span class="badge">(30 tools)</span></h4>
      <ul><li><a href="https://platerecognizer.com/" target="_blank" rel="noopener noreferrer">Plate Recognizer</a>: <span>Vehicle intelligence registry for looking up VIN numbers, license plates, and title records.</span></li><li><a href="http://www.worldlicenseplates.com/" target="_blank" rel="noopener noreferrer">License Plates of the World</a>: <span>Vehicle intelligence registry for looking up VIN numbers, license plates, and title records.</span></li><li><a href="http://www.vindecoderz.com/" target="_blank" rel="noopener noreferrer">VIN decoder</a>: <span>Vehicle intelligence registry for looking up VIN numbers, license plates, and title records.</span></li><li><a href="https://poctra.com/" target="_blank" rel="noopener noreferrer">Poctra.com</a>: <span>Vehicle intelligence registry for looking up VIN numbers, license plates, and title records.</span></li><li><a href="https://www.faxvin.com/" target="_blank" rel="noopener noreferrer">FAXVIN</a>: <span>Vehicle intelligence registry for looking up VIN numbers, license plates, and title records.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>IoT <span class="badge">(30 tools)</span></h4>
      <ul><li><a href="https://cse.google.com/cse?cx=013991603413798772546:gjcdtyiytey#gsc.tab=0" target="_blank" rel="noopener noreferrer">Webcam Search Engine</a>: <span>Investigative utility and OSINT resource for iot.</span></li><li><a href="http://www.insecam.org/" target="_blank" rel="noopener noreferrer">Insecam</a>: <span>Investigative utility and OSINT resource for iot.</span></li><li><a href="https://www.camhacker.com/" target="_blank" rel="noopener noreferrer">Camhacker.com</a>: <span>Investigative utility and OSINT resource for iot.</span></li><li><a href="https://www.earthcam.com/" target="_blank" rel="noopener noreferrer">EarthCam</a>: <span>Investigative utility and OSINT resource for iot.</span></li><li><a href="https://airportwebcams.net/" target="_blank" rel="noopener noreferrer">Airport Webcams</a>: <span>Investigative utility and OSINT resource for iot.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>PHONE <span class="badge">(27 tools)</span></h4>
      <ul><li><a href="https://inteltechniques.com/tools/Telephone.html" target="_blank" rel="noopener noreferrer">IntelTechniques Telephone</a>: <span>Michael Bazzell premier OSINT investigation methodology, training, and custom search engines.</span></li><li><a href="https://demo.phoneinfoga.crvx.fr" target="_blank" rel="noopener noreferrer">PhoneInfoga</a>: <span>Carrier lookup, HLR lookup, caller ID resolver, and reverse phone number directory.</span></li><li><a href="https://www.idcrawl.com/phone" target="_blank" rel="noopener noreferrer">Reverse Phone Lookup</a>: <span>Carrier lookup, HLR lookup, caller ID resolver, and reverse phone number directory.</span></li><li><a href="https://pypi.org/project/ignorant/" target="_blank" rel="noopener noreferrer">ignorant</a>: <span>Carrier lookup, HLR lookup, caller ID resolver, and reverse phone number directory.</span></li><li><a href="https://github.com/sundowndev/PhoneInfoga" target="_blank" rel="noopener noreferrer">PhoneInfoga</a>: <span>Carrier lookup, HLR lookup, caller ID resolver, and reverse phone number directory.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>BUSINESS <span class="badge">(27 tools)</span></h4>
      <ul><li><a href="https://cse.google.com/cse?cx=72ea9d8cfefc142d3" target="_blank" rel="noopener noreferrer">Companies &amp; Orgs Search Engine</a>: <span>Company registry, trademark lookup, corporate officers index, and business license verification.</span></li><li><a href="https://whaleslide.com/" target="_blank" rel="noopener noreferrer">WhaleSlide</a>: <span>Company registry, trademark lookup, corporate officers index, and business license verification.</span></li><li><a href="https://allpeople.com/" target="_blank" rel="noopener noreferrer">AllPeople</a>: <span>Company registry, trademark lookup, corporate officers index, and business license verification.</span></li><li><a href="https://www.corporationwiki.com/" target="_blank" rel="noopener noreferrer">Corporation Wiki</a>: <span>Company registry, trademark lookup, corporate officers index, and business license verification.</span></li><li><a href="https://public.flourish.studio/visualisation/3105919/" target="_blank" rel="noopener noreferrer">PA PPP Database</a>: <span>Company registry, trademark lookup, corporate officers index, and business license verification.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>PEOPLE <span class="badge">(26 tools)</span></h4>
      <ul><li><a href="https://www.idcrawl.com/" target="_blank" rel="noopener noreferrer">IDCrawl</a>: <span>Public records directory, address history aggregator, and contact intelligence tool for individuals.</span></li><li><a href="https://webmii.com/" target="_blank" rel="noopener noreferrer">WebMii</a>: <span>Public records directory, address history aggregator, and contact intelligence tool for individuals.</span></li><li><a href="https://intelx.io/tools?tab=person" target="_blank" rel="noopener noreferrer">Tools</a>: <span>Public records directory, address history aggregator, and contact intelligence tool for individuals.</span></li><li><a href="https://www.truepeoplesearch.com/" target="_blank" rel="noopener noreferrer">TruePeopleSearch</a>: <span>Public records directory, address history aggregator, and contact intelligence tool for individuals.</span></li><li><a href="https://www.peoplefinder.com/" target="_blank" rel="noopener noreferrer">Free People Search</a>: <span>Public records directory, address history aggregator, and contact intelligence tool for individuals.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>EMAIL <span class="badge">(26 tools)</span></h4>
      <ul><li><a href="https://identificator.space/" target="_blank" rel="noopener noreferrer">Identificator.space</a>: <span>Email permutation checker, MX validator, and breach footprint engine for verifying target emails.</span></li><li><a href="https://epieos.com/" target="_blank" rel="noopener noreferrer">Epieos Email Lookup</a>: <span>Reverse email and phone OSINT tool revealing associated Google, Skype, and social profiles.</span></li><li><a href="https://intelx.io/tools?tab=email" target="_blank" rel="noopener noreferrer">Intelligence X</a>: <span>Email permutation checker, MX validator, and breach footprint engine for verifying target emails.</span></li><li><a href="https://pypi.org/project/holehe/" target="_blank" rel="noopener noreferrer">holehe</a>: <span>Email permutation checker, MX validator, and breach footprint engine for verifying target emails.</span></li><li><a href="http://github.com/m4ll0k/Infoga" target="_blank" rel="noopener noreferrer">Infoga</a>: <span>Infoga - Email OSINT. Contribute to m4ll0k/Infoga development by creating an account on GitHub.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>EXTREMIST / FAR-RIGHT <span class="badge">(24 tools)</span></h4>
      <ul><li><a href="https://discordleaks.unicornriot.ninja/discord/" target="_blank" rel="noopener noreferrer">Unicorn Riot: Discord Leaks</a>: <span>Specialized monitoring tool, hate group tracker, or archive documenting radical movements.</span></li><li><a href="https://search.ddosecrets.com/data/" target="_blank" rel="noopener noreferrer">Data | DDoSecrets Search</a>: <span>Specialized monitoring tool, hate group tracker, or archive documenting radical movements.</span></li><li><a href="https://parler.adatascienti.st/research" target="_blank" rel="noopener noreferrer">Parler Archive Search</a>: <span>Specialized monitoring tool, hate group tracker, or archive documenting radical movements.</span></li><li><a href="https://projects.propublica.org/parler-capitol-videos/" target="_blank" rel="noopener noreferrer">Parler Capitol Videos</a>: <span>Specialized monitoring tool, hate group tracker, or archive documenting radical movements.</span></li><li><a href="https://whispers.ddosecrets.com/" target="_blank" rel="noopener noreferrer">Project Whispers</a>: <span>Specialized monitoring tool, hate group tracker, or archive documenting radical movements.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>NEWS <span class="badge">(23 tools)</span></h4>
      <ul><li><a href="https://cse.google.com/cse?cx=013991603413798772546:fvmtax6anhd" target="_blank" rel="noopener noreferrer">News Search Engine</a>: <span>Real-time global news aggregator, wire service monitor, or localized incident reporting portal.</span></li><li><a href="https://cse.google.com/cse/publicurl?cx=013991603413798772546:sipriovnbxq" target="_blank" rel="noopener noreferrer">Mailing List Archives Search Engine</a>: <span>Real-time global news aggregator, wire service monitor, or localized incident reporting portal.</span></li><li><a href="https://news.google.com/" target="_blank" rel="noopener noreferrer">Google News</a>: <span>Real-time global news aggregator, wire service monitor, or localized incident reporting portal.</span></li><li><a href="https://upstract.com/search" target="_blank" rel="noopener noreferrer">News Search</a>: <span>Real-time global news aggregator, wire service monitor, or localized incident reporting portal.</span></li><li><a href="http://newslookup.com/" target="_blank" rel="noopener noreferrer">Newslookup.com</a>: <span>Real-time global news aggregator, wire service monitor, or localized incident reporting portal.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>OPEN DIRECTORY <span class="badge">(23 tools)</span></h4>
      <ul><li><a href="https://cartographia.github.io/FilePhish/" target="_blank" rel="noopener noreferrer">FilePhish</a>: <span>Search tool for indexing and discovering open HTTP/FTP directories and cloud storage buckets.</span></li><li><a href="https://odfinder.github.io/" target="_blank" rel="noopener noreferrer">Open Directory Finder</a>: <span>Search tool for indexing and discovering open HTTP/FTP directories and cloud storage buckets.</span></li><li><a href="https://www.aware-online.com/en/osint-tools/filetype-search-tool/" target="_blank" rel="noopener noreferrer">Filetype search tool</a>: <span>Search tool for indexing and discovering open HTTP/FTP directories and cloud storage buckets.</span></li><li><a href="https://opendirsearch.abifog.com/" target="_blank" rel="noopener noreferrer">Opendirsearch.abifog.com</a>: <span>Search tool for indexing and discovering open HTTP/FTP directories and cloud storage buckets.</span></li><li><a href="https://archive-it.org/" target="_blank" rel="noopener noreferrer">Archive-it.org</a>: <span>Search tool for indexing and discovering open HTTP/FTP directories and cloud storage buckets.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>[CAN] GOVERNMENT <span class="badge">(23 tools)</span></h4>
      <ul><li><a href="https://lobbycanada.gc.ca/app/secure/ocl/lrs/do/advSrch?lang=eng" target="_blank" rel="noopener noreferrer">Advanced Registry Search</a>: <span>Canadian federal, provincial, and municipal government information and open data registry.</span></li><li><a href="https://www150.statcan.gc.ca/n1/en/type/data?HPA=1" target="_blank" rel="noopener noreferrer">Statistics Canada</a>: <span>Canadian federal, provincial, and municipal government information and open data registry.</span></li><li><a href="https://www.gazette.gc.ca/accueil-home-eng.html" target="_blank" rel="noopener noreferrer">Canada Gazette</a>: <span>Canadian federal, provincial, and municipal government information and open data registry.</span></li><li><a href="https://open.canada.ca/en/search/ati" target="_blank" rel="noopener noreferrer">Completed Access to Information Requests</a>: <span>Canadian federal, provincial, and municipal government information and open data registry.</span></li><li><a href="https://strategis.ic.gc.ca/eic/site/cid-dic.nsf/eng/home" target="_blank" rel="noopener noreferrer">Canadian Importers Database</a>: <span>Canadian federal, provincial, and municipal government information and open data registry.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>PRIVACY / SECURITY <span class="badge">(22 tools)</span></h4>
      <ul><li><a href="https://inteltechniques.com/workbook.html" target="_blank" rel="noopener noreferrer">Privacy Services by Michael Bazzell</a>: <span>This is the third step of a three-step process to request, freeze, and remove your personal information from within data broker and credit reporting services.</span></li><li><a href="https://privacyguides.org/" target="_blank" rel="noopener noreferrer">Privacy Guides</a>: <span>Operations security (OpSec) tool for hardening browsing sessions and blocking telemetry.</span></li><li><a href="https://ssd.eff.org/" target="_blank" rel="noopener noreferrer">Surveillance Self-Defense</a>: <span>Operations security (OpSec) tool for hardening browsing sessions and blocking telemetry.</span></li><li><a href="https://gofoss.net/" target="_blank" rel="noopener noreferrer">gofoss.net</a>: <span>Operations security (OpSec) tool for hardening browsing sessions and blocking telemetry.</span></li><li><a href="https://securityplanner.consumerreports.org/" target="_blank" rel="noopener noreferrer">Consumer Reports Security Planner</a>: <span>Operations security (OpSec) tool for hardening browsing sessions and blocking telemetry.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>SOURCE CODES <span class="badge">(21 tools)</span></h4>
      <ul><li><a href="https://cse.google.com/cse?cx=661713d0371832a02" target="_blank" rel="noopener noreferrer">Pastes Search Engine</a>: <span>Code search engine querying GitHub, GitLab, and source repos for exposed keys and commits.</span></li><li><a href="https://cse.google.com/cse?cx=006896442834264595052:fawrl1rug9e" target="_blank" rel="noopener noreferrer">Pastes Search Engine 2</a>: <span>Code search engine querying GitHub, GitLab, and source repos for exposed keys and commits.</span></li><li><a href="https://cse.google.com/cse?cx=1b053c8ec746d6611" target="_blank" rel="noopener noreferrer">GitHub Search Engine</a>: <span>Code search engine querying GitHub, GitLab, and source repos for exposed keys and commits.</span></li><li><a href="https://publicwww.com/" target="_blank" rel="noopener noreferrer">Source Code Search Engine</a>: <span>Code search engine querying GitHub, GitLab, and source repos for exposed keys and commits.</span></li><li><a href="https://recruitin.net/github.php" target="_blank" rel="noopener noreferrer">Google to search profiles on GitHub</a>: <span>Code search engine querying GitHub, GitLab, and source repos for exposed keys and commits.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>[CAN] CORPORATION <span class="badge">(21 tools)</span></h4>
      <ul><li><a href="https://rjsc.novascotia.ca/" target="_blank" rel="noopener noreferrer">RJSC Connect</a>: <span>Canadian corporate registry search for business ownership and corporate directors.</span></li><li><a href="https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html?locale=en_CA" target="_blank" rel="noopener noreferrer">Search for a Federal Corporation</a>: <span>Canadian corporate registry search for business ownership and corporate directors.</span></li><li><a href="https://federalcorporation.ca/" target="_blank" rel="noopener noreferrer">FederalCorporation</a>: <span>Canadian corporate registry search for business ownership and corporate directors.</span></li><li><a href="https://www.pxw2.snb.ca/card_online/cardsearch.aspx" target="_blank" rel="noopener noreferrer">Corporate Affairs Registry Database</a>: <span>Canadian corporate registry search for business ownership and corporate directors.</span></li><li><a href="https://beta.canadasbusinessregistries.ca/search" target="_blank" rel="noopener noreferrer">MRAS Business Registry Search</a>: <span>Canadian corporate registry search for business ownership and corporate directors.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>SECURE COMMUNICATION <span class="badge">(20 tools)</span></h4>
      <ul><li><a href="https://signal.org/" target="_blank" rel="noopener noreferrer">Signal</a>: <span>End-to-end encrypted messaging or zero-metadata channel for confidential communication.</span></li><li><a href="https://element.io/" target="_blank" rel="noopener noreferrer">Element</a>: <span>End-to-end encrypted messaging or zero-metadata channel for confidential communication.</span></li><li><a href="https://briarproject.org/" target="_blank" rel="noopener noreferrer">Briar</a>: <span>End-to-end encrypted messaging or zero-metadata channel for confidential communication.</span></li><li><a href="https://jami.net/" target="_blank" rel="noopener noreferrer">Jami.net</a>: <span>End-to-end encrypted messaging or zero-metadata channel for confidential communication.</span></li><li><a href="https://meet.jit.si/" target="_blank" rel="noopener noreferrer">Jitsi Meet</a>: <span>End-to-end encrypted messaging or zero-metadata channel for confidential communication.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>USERNAME <span class="badge">(19 tools)</span></h4>
      <ul><li><a href="https://whatsmyname.app/" target="_blank" rel="noopener noreferrer">WhatsMyName Web</a>: <span>Enumerates usernames across 500+ websites to discover digital footprints across platforms.</span></li><li><a href="https://analyzeid.com/username/" target="_blank" rel="noopener noreferrer">Username Checker</a>: <span>Username enumeration scanner searching hundreds of social networks and platforms for matching handles.</span></li><li><a href="https://www.idcrawl.com/username" target="_blank" rel="noopener noreferrer">Username Search</a>: <span>Username enumeration scanner searching hundreds of social networks and platforms for matching handles.</span></li><li><a href="https://intelx.io/tools?tab=username" target="_blank" rel="noopener noreferrer">Tools</a>: <span>Username enumeration scanner searching hundreds of social networks and platforms for matching handles.</span></li><li><a href="https://pypi.org/project/maigret/" target="_blank" rel="noopener noreferrer">maigret</a>: <span>Username enumeration scanner searching hundreds of social networks and platforms for matching handles.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>INSTAGRAM <span class="badge">(19 tools)</span></h4>
      <ul><li><a href="https://bibliogram.art/" target="_blank" rel="noopener noreferrer">Bibliogram.art</a>: <span>Instagram profile analyzer, story archiver, and hashtag mapping utility for visual intelligence.</span></li><li><a href="https://bib.actionsack.com/" target="_blank" rel="noopener noreferrer">Bibliogram</a>: <span>Instagram profile analyzer, story archiver, and hashtag mapping utility for visual intelligence.</span></li><li><a href="https://instahunt.co/" target="_blank" rel="noopener noreferrer">InstaHunt</a>: <span>Instagram profile analyzer, story archiver, and hashtag mapping utility for visual intelligence.</span></li><li><a href="https://cse.google.com/cse?cx=017261104271573007538:ffk_jpt64gy" target="_blank" rel="noopener noreferrer">Instagram Deep Photo Search Engine</a>: <span>Instagram profile analyzer, story archiver, and hashtag mapping utility for visual intelligence.</span></li><li><a href="https://gramho.com/" target="_blank" rel="noopener noreferrer">Instagram analyzer and viewer</a>: <span>Instagram profile analyzer, story archiver, and hashtag mapping utility for visual intelligence.</span></li></ul>
    </div>
    

    <div class="seo-cat-block">
      <h4>GOOGLE CSE <span class="badge">(19 tools)</span></h4>
      <ul><li><a href="https://cse.google.com/cse?cx=005797772976587943970:3tu7im1-rdg#gsc.tab=0" target="_blank" rel="noopener noreferrer">Homepage Search Engine</a>: <span>Custom Search Engine curated by security researchers targeting specific archives and documents.</span></li><li><a href="https://cse.google.com/cse?cx=005797772976587943970:g-6ohngosio#gsc.tab=0" target="_blank" rel="noopener noreferrer">Amazon Cloud Search Engine</a>: <span>Custom Search Engine curated by security researchers targeting specific archives and documents.</span></li><li><a href="https://cse.google.com/cse?cx=009462381166450434430:vggeu3dhhgg#gsc.tab=0" target="_blank" rel="noopener noreferrer">Google CSE instances Search Engine</a>: <span>Custom Search Engine curated by security researchers targeting specific archives and documents.</span></li><li><a href="https://cse.google.com/cse?cx=013991603413798772546:zu7epjqvunu" target="_blank" rel="noopener noreferrer">Robots.txt Search Engine</a>: <span>Custom Search Engine curated by security researchers targeting specific archives and documents.</span></li><li><a href="https://cse.google.com/cse?cx=017261104271573007538:magh-vr6t6g#gsc.tab=0" target="_blank" rel="noopener noreferrer">Short URL Search Engine</a>: <span>Custom Search Engine curated by security researchers targeting specific archives and documents.</span></li></ul>
    </div>
    
        </div>
      </div>

      <!-- SOCIAL SHARE BANNER -->
      <div class="share-banner">
        <div>
          <strong style="color:#ffffff; font-size:1.1rem; display:block;">Share This OSINT Toolkit</strong>
          <span style="color:var(--os-text-muted); font-size:0.9rem;">Help fellow researchers, cybersecurity analysts, and journalists discover free investigation resources.</span>
        </div>
        <div class="share-btns">
          <a class="share-btn share-x" href="https://twitter.com/intent/tweet?text=Explore%20the%20Ultimate%20OSINT%20Toolkit%20%281%2C450%2B%20Free%20Investigation%20Tools%29%20by%20@rkoots&url=https://rkoots.github.io/tools/osint/" target="_blank" rel="noopener noreferrer"><i class="fab fa-x-twitter"></i> Tweet</a>
          <a class="share-btn share-li" href="https://www.linkedin.com/sharing/share-offsite/?url=https://rkoots.github.io/tools/osint/" target="_blank" rel="noopener noreferrer"><i class="fab fa-linkedin"></i> LinkedIn</a>
          <a class="share-btn share-rd" href="https://reddit.com/submit?url=https://rkoots.github.io/tools/osint/&title=The%20Ultimate%20OSINT%20Toolkit%20-%201400%2B%20Verified%20Tools" target="_blank" rel="noopener noreferrer"><i class="fab fa-reddit-alien"></i> Reddit</a>
        </div>
      </div>
    </article>

  </div>
</div>

<!-- Load Dedicated OSINT Data Bundle -->
<script src="{{ '/assets/js/osint-data.js' | relative_url }}"></script>

<!-- ==========================================================================
     INTERACTIVE APPLICATION ENGINE
     ========================================================================== -->
<script>
(function() {
  'use strict';

  // State Management
  let allTools = [];
  let filteredTools = [];
  let renderedCount = 0;
  const CHUNK_SIZE = 48;
  let activeGroup = 'ALL';
  let activeSubcat = 'ALL';
  let activeSort = 'default';
  let activeSearch = '';
  let favorites = new Set();
  let isListView = false;

  // DOM Elements
  const container = document.getElementById('tools-container');
  const searchInput = document.getElementById('osint-search');
  const clearSearchBtn = document.getElementById('clear-search');
  const subcatSelect = document.getElementById('subcat-select');
  const sortSelect = document.getElementById('sort-select');
  const domainTabs = document.getElementById('domain-tabs');
  const resultsCountEl = document.getElementById('results-count');
  const currentScopeEl = document.getElementById('current-scope');
  const emptyState = document.getElementById('empty-state');
  const loadMoreWrap = document.getElementById('load-more-wrap');
  const loadMoreRemEl = document.getElementById('load-more-remaining');
  const favCountEl = document.getElementById('fav-count');
  const viewGridBtn = document.getElementById('view-grid');
  const viewListBtn = document.getElementById('view-list');
  const themeToggleBtn = document.getElementById('theme-toggle');
  const toast = document.getElementById('osint-toast');
  const toastMsg = document.getElementById('toast-msg');

  // Load Favorites from localStorage
  function loadFavorites() {
    try {
      const saved = localStorage.getItem('osint_favorites_v1');
      if (saved) {
        favorites = new Set(JSON.parse(saved));
      }
    } catch (e) {
      favorites = new Set();
    }
    updateFavCounter();
  }

  function saveFavorites() {
    try {
      localStorage.setItem('osint_favorites_v1', JSON.stringify(Array.from(favorites)));
    } catch (e) {}
    updateFavCounter();
  }

  function updateFavCounter() {
    if (favCountEl) favCountEl.textContent = favorites.size;
  }

  // Initialize App
  function init() {
    loadFavorites();
    
    // Check if OSINT_DATA bundle loaded from script
    if (window.OSINT_DATA && Array.isArray(window.OSINT_DATA)) {
      allTools = window.OSINT_DATA;
      setupApp();
    } else {
      // Fallback: Fetch JSON
      fetch('/assets/data/osint-tools.json')
        .then(r => r.json())
        .then(data => {
          allTools = data;
          setupApp();
        })
        .catch(err => {
          console.error('Failed to load OSINT tools:', err);
        });
    }
  }

  function setupApp() {
    bindEvents();
    applyFilters();
  }

  // Event Listeners
  function bindEvents() {
    // Search input debounce
    let debounceTimer;
    searchInput.addEventListener('input', function(e) {
      clearTimeout(debounceTimer);
      activeSearch = e.target.value.trim().toLowerCase();
      clearSearchBtn.style.display = activeSearch ? 'block' : 'none';
      debounceTimer = setTimeout(applyFilters, 150);
    });

    clearSearchBtn.addEventListener('click', function() {
      searchInput.value = '';
      activeSearch = '';
      clearSearchBtn.style.display = 'none';
      applyFilters();
      searchInput.focus();
    });

    // Subcategory select
    subcatSelect.addEventListener('change', function(e) {
      activeSubcat = e.target.value;
      applyFilters();
    });

    // Sort select
    sortSelect.addEventListener('change', function(e) {
      activeSort = e.target.value;
      applyFilters();
    });

    // Domain Group Tabs
    domainTabs.addEventListener('click', function(e) {
      const tab = e.target.closest('.domain-tab');
      if (!tab) return;
      document.querySelectorAll('.domain-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      activeGroup = tab.getAttribute('data-group');
      applyFilters();
    });

    // Grid vs List view
    viewGridBtn.addEventListener('click', function() {
      isListView = false;
      viewGridBtn.classList.add('active');
      viewListBtn.classList.remove('active');
      container.classList.remove('list-mode');
    });

    viewListBtn.addEventListener('click', function() {
      isListView = true;
      viewListBtn.classList.add('active');
      viewGridBtn.classList.remove('active');
      container.classList.add('list-mode');
    });

    // Day / Night Theme Toggle
    themeToggleBtn.addEventListener('click', function() {
      document.body.classList.toggle('daylight-lab');
      const isDay = document.body.classList.contains('daylight-lab');
      themeToggleBtn.innerHTML = isDay ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
      themeToggleBtn.title = isDay ? "Switch to Cyber Night Theme" : "Switch to Daylight Lab Theme";
    });

    // FAQ Accordion click
    document.querySelectorAll('.faq-question').forEach(q => {
      q.addEventListener('click', function() {
        this.parentElement.classList.toggle('active');
      });
    });
  }

  // Filter & Sorting Logic
  function applyFilters() {
    filteredTools = allTools.filter(t => {
      // Domain Group filter
      if (activeGroup === 'FAVORITES') {
        if (!favorites.has(t.url)) return false;
      } else if (activeGroup !== 'ALL' && t.group !== activeGroup) {
        return false;
      }

      // Subcategory filter
      if (activeSubcat !== 'ALL' && t.cat !== activeSubcat) {
        return false;
      }

      // Search keyword filter
      if (activeSearch) {
        const inName = t.name.toLowerCase().includes(activeSearch);
        const inDesc = t.desc.toLowerCase().includes(activeSearch);
        const inUrl = t.url.toLowerCase().includes(activeSearch);
        const inCat = t.cat.toLowerCase().includes(activeSearch);
        if (!inName && !inDesc && !inUrl && !inCat) return false;
      }

      return true;
    });

    // Sorting
    if (activeSort === 'az') {
      filteredTools.sort((a,b) => a.name.localeCompare(b.name));
    } else if (activeSort === 'za') {
      filteredTools.sort((a,b) => b.name.localeCompare(a.name));
    } else if (activeSort === 'cat') {
      filteredTools.sort((a,b) => a.cat.localeCompare(b.cat) || a.name.localeCompare(b.name));
    }

    // Update Counts & Meta
    resultsCountEl.innerHTML = `Showing <strong>${filteredTools.length.toLocaleString()}</strong> of <strong>${allTools.length.toLocaleString()}</strong> tools`;
    currentScopeEl.textContent = activeGroup === 'ALL' ? 'Scope: All Domains' : `Scope: ${activeGroup}`;

    // Render Cards
    container.innerHTML = '';
    renderedCount = 0;

    if (filteredTools.length === 0) {
      emptyState.style.display = 'block';
      loadMoreWrap.style.display = 'none';
    } else {
      emptyState.style.display = 'none';
      renderMoreTools();
    }
  }

  // Render Chunk of Tools
  function renderMoreTools() {
    const nextCount = Math.min(renderedCount + CHUNK_SIZE, filteredTools.length);
    const fragment = document.createDocumentFragment();

    for (let i = renderedCount; i < nextCount; i++) {
      const tool = filteredTools[i];
      const card = createToolCard(tool, i);
      fragment.appendChild(card);
    }

    container.appendChild(fragment);
    renderedCount = nextCount;

    const remaining = filteredTools.length - renderedCount;
    if (remaining > 0) {
      loadMoreWrap.style.display = 'block';
      loadMoreRemEl.textContent = remaining.toLocaleString();
    } else {
      loadMoreWrap.style.display = 'none';
    }
  }

  function loadAllTools() {
    const fragment = document.createDocumentFragment();
    for (let i = renderedCount; i < filteredTools.length; i++) {
      const tool = filteredTools[i];
      const card = createToolCard(tool, i);
      fragment.appendChild(card);
    }
    container.appendChild(fragment);
    renderedCount = filteredTools.length;
    loadMoreWrap.style.display = 'none';
  }

  // Extract Clean Domain Name
  function getDomain(url) {
    try {
      return new URL(url).hostname.replace('www.', '');
    } catch (e) {
      return url;
    }
  }

  // Create Individual Tool Card DOM Element
  function createToolCard(tool, index) {
    const card = document.createElement('article');
    card.className = 'osint-card';
    card.id = `tool-${index}`;

    const domain = getDomain(tool.url);
    const isStarred = favorites.has(tool.url);
    const initial = (tool.name.replace(/[^a-zA-Z0-9]/g, '').slice(0, 2) || 'OS').toUpperCase();

    // Icon handling
    let iconHtml = '';
    if (tool.icon && !tool.icon.includes('/fa/bookmark')) {
      iconHtml = `<img class="tool-icon-img" src="${tool.icon}" alt="${htmlEscape(tool.name)}" loading="lazy" onerror="this.onerror=null;this.parentElement.innerHTML='<span class=\'tool-icon-fallback\'>${initial}</span>'">`;
    } else {
      iconHtml = `<span class="tool-icon-fallback">${initial}</span>`;
    }

    card.innerHTML = `
      <div class="card-top">
        <div class="tool-icon-frame">
          ${iconHtml}
        </div>
        <div class="card-header-info">
          <h3 class="tool-name">
            <a href="${tool.url}" target="_blank" rel="noopener noreferrer">${htmlEscape(tool.name)}</a>
          </h3>
          <div class="tool-domain">${domain}</div>
        </div>
        <button class="btn-star ${isStarred ? 'starred' : ''}" title="${isStarred ? 'Remove from favorites' : 'Add to favorites'}" aria-label="Favorite tool">
          <i class="${isStarred ? 'fas' : 'far'} fa-star"></i>
        </button>
      </div>

      <div class="card-badges">
        <span class="badge-tag badge-group">${htmlEscape(tool.group)}</span>
        <span class="badge-tag badge-cat">${htmlEscape(tool.cat)}</span>
      </div>

      <p class="tool-desc">${htmlEscape(tool.desc)}</p>

      <div class="card-actions">
        <a href="${tool.url}" target="_blank" rel="noopener noreferrer" class="card-btn card-btn-visit">
          <span>Open Tool</span> <i class="fas fa-external-link-alt"></i>
        </a>
        <button class="card-btn card-btn-copy" title="Copy Tool Link">
          <i class="far fa-copy"></i>
        </button>
      </div>
    `;

    // Star button click
    const starBtn = card.querySelector('.btn-star');
    starBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (favorites.has(tool.url)) {
        favorites.delete(tool.url);
        starBtn.classList.remove('starred');
        starBtn.innerHTML = '<i class="far fa-star"></i>';
        showToast('Removed from favorites');
      } else {
        favorites.add(tool.url);
        starBtn.classList.add('starred');
        starBtn.innerHTML = '<i class="fas fa-star"></i>';
        showToast('Saved to favorites');
      }
      saveFavorites();
      if (activeGroup === 'FAVORITES') applyFilters();
    });

    // Copy button click
    const copyBtn = card.querySelector('.card-btn-copy');
    copyBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      copyToClipboard(tool.url);
      showToast(`Copied ${tool.name} URL!`);
    });

    return card;
  }

  function htmlEscape(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // Clipboard copy
  function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text);
    } else {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
    }
  }

  // Toast feedback
  let toastTimer;
  function showToast(msg) {
    toastMsg.textContent = msg;
    toast.classList.add('visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove('visible');
    }, 2500);
  }

  // Global functions exposed to window
  window.resetAllFilters = function() {
    searchInput.value = '';
    activeSearch = '';
    activeSubcat = 'ALL';
    activeGroup = 'ALL';
    activeSort = 'default';
    subcatSelect.value = 'ALL';
    sortSelect.value = 'default';
    clearSearchBtn.style.display = 'none';
    document.querySelectorAll('.domain-tab').forEach(t => t.classList.remove('active'));
    document.querySelector('.domain-tab[data-group="ALL"]').classList.add('active');
    applyFilters();
  };

  window.renderMoreTools = renderMoreTools;
  window.loadAllTools = loadAllTools;

  window.pickRandomTool = function() {
    if (allTools.length === 0) return;
    const randomTool = allTools[Math.floor(Math.random() * allTools.length)];
    searchInput.value = randomTool.name;
    activeSearch = randomTool.name.toLowerCase();
    activeGroup = 'ALL';
    activeSubcat = 'ALL';
    clearSearchBtn.style.display = 'block';
    applyFilters();

    setTimeout(() => {
      const firstCard = container.querySelector('.osint-card');
      if (firstCard) {
        firstCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        firstCard.classList.add('highlight-pulse');
        showToast(`Random Discovery: ${randomTool.name}!`);
        setTimeout(() => firstCard.classList.remove('highlight-pulse'), 4000);
      }
    }, 200);
  };

  // Recon Pivot Launcher
  window.launchPivot = function(engine) {
    const target = document.getElementById('recon-target').value.trim();
    if (!target) {
      showToast('Please enter a target query first!');
      document.getElementById('recon-target').focus();
      return;
    }

    const q = encodeURIComponent(target);
    let url = '';

    switch(engine) {
      case 'dork':
        url = `https://www.google.com/search?q=${encodeURIComponent('"' + target + '" (inurl:admin | filetype:pdf | site:linkedin.com | site:pastebin.com)')}`;
        break;
      case 'shodan':
        url = `https://www.shodan.io/search?query=${q}`;
        break;
      case 'virustotal':
        url = `https://www.virustotal.com/gui/search/${q}`;
        break;
      case 'wayback':
        url = `https://web.archive.org/web/*/${q}`;
        break;
      case 'whatsmyname':
        url = `https://whatsmyname.app/?q=${q}`;
        break;
      case 'epieos':
        url = `https://epieos.com/?q=${q}`;
        break;
      case 'cyberchef':
        url = `https://gchq.github.io/CyberChef/#input=${encodeURIComponent(btoa(unescape(encodeURIComponent(target))))}`;
        break;
      case 'whois':
        url = `https://viewdns.info/whois/?domain=${q}`;
        break;
    }

    if (url) {
      window.open(url, '_blank', 'noopener,noreferrer');
      showToast(`Pivoting to ${engine.toUpperCase()}...`);
    }
  };

  // Export Bookmarks HTML (Netscape Bookmark Format)
  window.exportBookmarksHTML = function() {
    const grouped = {};
    allTools.forEach(t => {
      if (!grouped[t.group]) grouped[t.group] = {};
      if (!grouped[t.group][t.cat]) grouped[t.group][t.cat] = [];
      grouped[t.group][t.cat].push(t);
    });

    let html = `<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>OSINT Hub 2026 Bookmarks</TITLE>
<H1>OSINT Hub 2026 - 1,450+ Investigation Tools</H1>
<DL><p>
`;

    for (const [groupName, catDict] of Object.entries(grouped)) {
      html += `    <DT><H3>${htmlEscape(groupName)}</H3>\n    <DL><p>\n`;
      for (const [catName, toolList] of Object.entries(catDict)) {
        html += `        <DT><H3>${htmlEscape(catName)}</H3>\n        <DL><p>\n`;
        toolList.forEach(tool => {
          html += `            <DT><A HREF="${tool.url}" ADD_DATE="${Math.floor(Date.now() / 1000)}" LAST_MODIFIED="${Math.floor(Date.now() / 1000)}">${htmlEscape(tool.name)}</A>\n`;
        });
        html += `        </DL><p>\n`;
      }
      html += `    </DL><p>\n`;
    }

    html += `</DL><p>\n`;

    const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
    const downloadUrl = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = downloadUrl;
    a.download = 'OSINT-Hub-2026-Bookmarks.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(downloadUrl);
    showToast('Downloaded Browser Bookmarks HTML!');
  };

  // Export JSON
  window.exportJSON = function() {
    const blob = new Blob([JSON.stringify(allTools, null, 2)], { type: 'application/json' });
    const downloadUrl = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = downloadUrl;
    a.download = 'osint-tools-2026.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(downloadUrl);
    showToast('Downloaded OSINT Tools JSON!');
  };

  // Boot
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
</script>
