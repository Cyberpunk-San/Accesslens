# AccessLens Backend Technical Guide

The AccessLens backend is a high-performance auditing suite designed for modular expansion and high-fidelity analysis.

---

## Core Architecture

### 1. API Intelligence (FastAPI)
Handles RESTful communication, validation, and async task orchestration.
- **V1 Router**: Standardized endpoints for audits and engine discovery.
- **BackgroundTasks**: Offloads compute-heavy analysis without blocking the user.
- **Rate Limiting**: Custom sliding-window middleware to prevent abuse.

### 2. The Orchestration Layer
The **Audit Orchestrator** manages the "lifecycle of discovery":
1.  **Lease Page**: Requests an isolated Chromium page from the `BrowserManager`.
2.  **Snapshot**: Captures the raw AX-Tree, DOM, and visual state.
3.  **Parallel Execution**: Triggers all selected engines simultaneously.
4.  **Issue Synthesis**: Deduplicates overlapping findings and normalizes scoring.

### 3. Engine Registry & Aliasing
A dynamic system that maps user-friendly names (e.g., `wcag`) to robust internal implementations (`WCAGDeterministicEngine`). This allows for decoupled engine development and versioning.

---

## Specialized Analysis Engines

AccessLens uses 7 distinct layers of analysis:

| Engine | Strategy | Detection Scope |
| :--- | :--- | :--- |
| **WCAG** | Deterministic | Industry-standard `axe-core` violations. |
| **Structural** | DOM-Traversing | Semantic landmarks, heading order, ARIA roles. |
| **Contrast** | Computed CSS | Real-time color contrast in various interactive states. |
| **Navigation** | Simulation | Tab-order logic, keyboard traps, focus indicators. |
| **Form** | Validation | Label-input linking, error state focus, placeholder UX. |
| **Heuristic** | Rule-Based | Link text quality, reading complexity, redundant attributes. |
| **AI** | Multimodal | Contextual remediation using VLM vision pipelines. |

---

## Data & Persistence

- **SQLite**: Local relational storage for audit results and metric history.
- **Redis (Optional)**: Used as a cache layer for task status and intermediate snapshots.
- **Blob Storage**: Local `data/` folder stores compressed screenshots and AX-Tree JSONs.

---

## Testing and Quality
The backend maintains a >90% coverage suite using `pytest-asyncio`, covering:
- **Engine Accuracy**: Unit tests for every detection rule.
- **Concurrency**: Stress-testing engine execution under load.
---

## Further Documentation
To understand the backend in more detail, including file-by-file explanations and engine internals, please visit [backend/README.md](../backend/README.md).
