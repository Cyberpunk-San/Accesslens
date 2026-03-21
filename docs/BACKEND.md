# AccessLens Backend Architecture

The AccessLens backend is a high-performance auditing engine built with **Python**, **FastAPI**, and **Playwright**. It orchestrates multiple analysis engines to provide a comprehensive accessibility report.

## Core Components

### 1. API Layer (FastAPI)
The entry point for all frontend requests. It handles:
- **Audit Submission**: Accepts URLs and configuration options.
- **Background Tasks**: Offloads intensive analysis to an async orchestrator.
- **Data Retrieval**: Serves audit results and historical metrics from SQLite.

### 2. Audit Orchestrator
The "brain" of the backend. It manages the lifecycle of an audit:
- Initialize the target page.
- Parallelize execution of multiple deterministic engines.
- Synthesize all findings into a unified, de-duplicated issue list.
- Calculate final compliance scores and confidence metrics.

### 3. Browser Manager
A robust pooling system for **Playwright/Chromium**:
- Handles browser lifecycle and context isolation.
- Ensures efficient resource usage by reusing browser instances where possible.

## Analysis Engines

AccessLens uses a multi-engine strategy to ensure maximum coverage:

- **WCAG Engine**: Powered by **axe-core**, the industry standard for programmatic accessibility testing.
- **Contrast Engine**: Evaluates computed CSS colors, including hover and focus states, to find contrast failures.
- **Structural Engine**: Analyzes heading hierarchy, ARIA landmarks, and semantic HTML markers.
- **Form Engine**: Validates label-input associations and ARIA descriptions for interactive fields.
- **Heuristic Engine**: Catches UX anti-patterns like repetitive link text and estimates reading complexity.
- **Navigation Engine**: Simulates keyboard interactions to detect focus traps and tab order issues.

## Data Persistence

- **Report Storage**: Uses **SQLite** for lightweight, persistent result storage.
- **File Storage**: Stores screenshots and snapshots in the `/data` directory.

## Design Patterns

- **Unified Issue Format**: All engines return a standardized `UnifiedIssue` object, simplifying the frontend consumption.
- **Engine Plugin System**: New analysis engines can be added by implementing the `BaseEngine` interface.
- **Async Execution**: Non-blocking I/O ensures the system can handle concurrent audit requests efficiently.
