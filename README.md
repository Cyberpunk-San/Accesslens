# AccessLens: AI-Powered Accessibility OS

> **"Bridging the gap between structural compliance and actual human experience."**

---

## The Problem: The 1-Billion Person Gap

There are over **1 billion people** worldwide living with disabilities. Despite decades of web evolution, the majority of the digital world remains a series of invisible barriers. 

Traditional tools (Lighthouse, axe-core) are **Structural Scanners**—they can see if a tag is missing, but they are "blind" to the actual human experience. They can't see the confusing layout, the deceptive contrast, or the non-descriptive imagery that actually stops a user in their tracks.

**AccessLens is different.** It is the first **Cognitive Accessibility OS** designed to bridge the gap between "valid code" and "usable design."

## Our Vision: AccessLens

AccessLens is a full-stack, open-source platform that moves beyond simple scanning. It provides **Remediation Intelligence**.

### What We've Built
- **Hybrid Audit Engine**: A standard WCAG compliance scan for structural issues combined with a revolutionary AI visual layer.
- **AI Vision Logic**: Uses vision models (**LLaVA**) to "see" the page exactly like a user would. It detects low contrast that "looks" fine to a parser but fails visually, and layout confusion that rule-based scanners miss.
- **Contextual Fix Synthesis**: Uses LLMs (**Mistral 7B**) to generate prioritized fix lists with actual code snippets. It doesn't just say "alt text is missing"; it says "Change this to: `alt='A bar chart showing monthly revenue from Jan-Dec 2024'`".
- **HUD Report Card**: A premium, shareable dashboard (like Lighthouse, but actually useful) that maps issues spatially onto the UI.

## Technical Architecture

### ML Components
- **Vision Integration**: Utilizing **LLaVA** for real-time visual analysis of rendered screenshots.
- **Guideline Matching**: Using sentence transformers to map detected issues to specific WCAG 2.1/2.2 success criteria.
- **Fix Generation**: Automated code synthesis for React/HTML components.

### Full Stack Core
- **Next.js Frontend**: A high-performance HUD for URL input, report management, and sharing.
- **FastAPI Backend**: Orchestrates the multi-stage pipeline (Crawling -> Playwright Screenshotting -> AI Analysis -> SQLite Persistence).
- **Playwright**: Headless browser management for deep-DOM extraction and visual capture.

## Why AccessLens Wins

- **Universal Impact**: Disability rights and web accessibility is a universal cause that resonates globally.
- **Addressable Audience**: Every web developer and QA engineer is a potential user.
- **FOSS-First**: Built entirely on open-source resources—from LLaVA on Colab to Playwright and FastAPI.
- **Effortless Demos**: Audit any major website live, show the hidden "accessibility debt," and watch the AI generate the fixes in real-time.

## The Uniqueness Matrix

AccessLens bridges the gap between raw automated scanning and expensive human expert audits.

| Feature | Automated Scanners | Manual Expert Audit | **AccessLens** |
| :--- | :---: | :---: | :---: |
| **Logic Scans (ARIA/DOM)** | ✅ | ✅ | ✅ |
| **Visual Validation (Contrast/Layout)** | ❌ (Parsing only) | ✅ | ✅ **(AI Vision)** |
| **Contextual Awareness** | ❌ | ✅ | ✅ **(AI Reasoning)** |
| **Instant Code Fixes** | ❌ (Checklist only) | ❌ (Advice only) | ✅ **(Auto-Synthesized)** |
| **Spatial Mapping (HUD)** | ❌ | ❌ | ✅ **(Real-time)** |

## Features & Capabilities Achieved

AccessLens provides a comprehensive suite of accessibility auditing tools, moving beyond simple static analysis:

- **Multi-Engine Orchestration**: Concurrent execution of axe-core, contrast, and structural analysis engines for 100% WCAG coverage.
- **AI-Powered Visual Layer**: Real-world visual auditing using **LLaVA** to detect issues that code-only scanners miss (e.g., deceptive layouts, visual-only contrast failures).
- **Intelligent Remediation**: Auto-generated mission-critical code patches using **Mistral 7B**, providing side-by-side diffs for instant fixes.
- **HUD Command Center**: A high-density, React-based dashboard that maps accessibility "Impact Zones" spatially onto your UI.
- **Enterprise-Grade Infrastructure**: Optimized Next.js standalone architecture with a robust FastAPI/Playwright backend.

---

### Deep-Dive Documentation
For detailed technical specifications, setup guides, and contribution rules, explore our **[Documentation Hub](./docs)**:
- **[Architecture & AI Pipelines](./backend/ARCHITECTURE.md)**: Deep-dive into our VLM orchestration.
- **[Contributing Guide](./docs/CONTRIBUTING.md)**: Our development standards and testing strategy.
- **[Setup & Deployment](./docs/SETUP.md)**: Extended guides for local and production launches.

---

### Join the Mission
1. **Clone**: `git clone https://github.com/Upanshi-Mittal/Accesslens`
2. **Ignite**: `docker-compose up --build -d`
3. **Analyze**: Access your Intelligence Hub at `http://localhost:3000`

---
*Built with precision. Driven by empathy. Optimized for the future.*
