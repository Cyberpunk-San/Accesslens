# AccessLens System Architecture

AccessLens is a high-performance accessibility auditing platform built on a modular "Collective Intelligence" architecture. It orchestrates deterministic heuristic engines with modern Vision-Language Models (VLMs) to provide contextual remediation.

---

## Technical Stack

- **Backend**: FastAPI (Python 3.10)
- **Frontend**: Next.js 14 (App Router)
- **Browser Automation**: Playwright (Headless Chromium)
- **Database**: SQLite (Local persistence)
- **Cache**: Redis (Task status & result caching)

---

## System Orchestration

The system follows an asynchronous request-response lifecycle to ensure high availability during deep audits.

```mermaid
graph TD
    A[Frontend Dashboard] -->|POST /audit| B(FastAPI Router)
    B -->|Task ID| A
    B -->|Enqueue| C[Audit Orchestrator]
    C -->|Browser Launch| D[Playwright Instance]
    D -->|Extract| E[DOM & AXTree]
    D -->|Capture| F[Visual Screenshots]
    E & F -->|Async Analysis| G[Analysis Registry]
    G -->|Engine Result| H[Data Aggregator]
    H -->|AI Synthesis| I[AI Service]
    I -->|Remediation Strategy| J[Report Storage]
    J -->|Cache| K[Redis]
```

---

## Analysis Engines (Collective Intelligence)

The core strength of AccessLens lies in its **Engine Registry**. Each engine is an isolated module that implements the `BaseAccessibilityEngine` interface.

1. **AxeEngine**: Leverages `axe-core` for industry-standard WCAG 2.1 compliance.
2. **ContrastEngine**: Performs high-fidelity color contrast analysis on rendered components.
3. **StructureEngine**: Deep-scans the DOM for semantic integrity and landmark consistency.
4. **HeuristicEngine**: Uses custom deterministic rules for keyboard navigability and interactable focus states.

---

## AI Integration Layer

Unlike traditional scanners, AccessLens uses a two-stage computer vision and code synthesis pipeline.

### 1. Vision Recognition (LLaVA)
AccessLens "sees" the UI using **LLaVA**. This engine identifies visual barriers that standard code parsers miss:
- Deceptive design patterns.
- Overlapping elements.
- Meaningful information conveyed solely through visual cues (e.g., status icons without labels).

### 2. Refactoring Synthesis (Mistral 7B)
The system uses **Mistral 7B** to translate raw violations into production-ready code. Instead of vague warnings, it provides **Synthetic Code Patches**—accurate diffs showing exactly how to refactor the offending component.

---

## Data Strategy

- **Deduplication**: The Orchestrator uses fuzzy matching to ensure that identical issues across multiple engines are unified into a single report.
- **Persistence**: Audit results and AX-Tree snapshots are stored in SQLite, while high-resolution screenshots are managed in the `storage/` directory.
- **Caching**: Global audit status is synchronized via Redis to provide real-time updates to the dashboard via polling.

---

## Evolutionary Roadmap

- **Multi-Page Crawling**: Expanding analysis from single-page snapshots to full-site recursive audits.
- **Automated PR Generation**: Directly injecting fix suggestions into CI/CD pipelines.
- **Enterprise Reporting**: PDF export and team-based compliance dashboards.

---
*Built with precision for the modern web.*
