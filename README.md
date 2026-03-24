# AccessLens

*Bridges the gap between valid code and usable design by detecting real-world accessibility issues and generating fixes.*

---

## The Problem: The Accessibility Gap

Over **1 billion people** live with disabilities, yet much of the web remains inaccessible.

Traditional tools like Lighthouse and axe-core check code compliance—but miss real user experience. They fail to detect confusing layouts, poor contrast in dynamic states, and non-descriptive content that actually blocks users.

**AccessLens solves this gap.** It detects real-world accessibility issues and generates actionable fixes by analyzing how interfaces are actually experienced—not just how they are coded.

---

## System Capabilities

### 1. Multi-Engine Orchestration
AccessLens executes seven specialized engines in parallel to provide a comprehensive audit:
- **WCAG Deterministic**: Industry-standard rule validation using `axe-core`.
- **Structural Heuristics**: Analysis of semantic landmarks, heading hierarchy, and ARIA roles.
- **Contrast Correlation**: Precise measurement of color ratios across rendered gradients and interactive states.
- **Navigation & Forms**: Simulation of keyboard tab-order and form-label association logic.
- **UX Heuristics**: Detection of repetitive link text and content reading complexity.

### 2. Computer Vision Integration (LLaVA)
Utilizing the **LLaVA** vision model, AccessLens performs perceptual analysis on high-resolution viewport screenshots:
- **Layout Validation**: Detects overlapping elements or deceptive visual hierarchies.
- **Visual Contrast**: Validates contrast in complex, non-text UI elements.
- **Semantic Imagery**: Generates high-fidelity alternative text descriptions based on visual context.

### 3. AX-Tree Synchronization & Visualization
AccessLens extracts the browser's native **Accessibility Tree (AX-Tree)** and synchronizes it with the visual HUD. This allows developers to inspect how the browser represents the page to assistive technologies in real-time.

### 4. Automated Code Remediation (Mistral 7B)
Powered by **Mistral 7B**, the remediation engine converts detected violations into localized **React and HTML code patches**. It analyzes the surrounding DOM context to generate side-by-side diffs, simplifying the implementation of fixes.

---

## System Architecture

AccessLens follows a modular, layer-driven architecture designed for high-concurrency auditing and AI synthesis.

```mermaid
graph TB
    subgraph Client_Layer [Client Layer]
        HUD[Cyber-HUD Dashboard]
        UX[Next.js / Framer Motion]
    end

    subgraph Service_Orchestration [Service & Orchestration]
        API[FastAPI Orchestrator]
        Reg[Engine Registry]
        Browser[Headless Browser Engine]
        
        subgraph Analysis_Engines [The 7 Layers of Analysis]
            WCAG[1. WCAG Deterministic]
            STR[2. Structural Landmark]
            CON[3. Contrast Correlation]
            NAV[4. Keyboard Navigation]
            FORM[5. Form Validation]
            HEUR[6. UX Heuristic]
            AI_E[7. AI Perceptual]
        end
    end

    subgraph Intelligence_Layer [Intelligence & Inference]
        LLAVA[LLaVA / Vision]
        MISTRAL[Mistral 7B / Code Fixes]
    end

    subgraph Persistence_Layer [Data & Infrastructure]
        REDIS[(Redis Cache / State)]
        SQLITE[(SQLite / Reports)]
    end

    HUD <-->|REST API| API
    API -->|Load| Reg
    API -->|Control| Browser
    
    Browser -->|Viewport Render| LLAVA
    Browser -->|DOM Tree| Reg
    
    Reg -->|Execution| Analysis_Engines
    AI_E <-->|Context| LLAVA
    Analysis_Engines -->|Matrix| MISTRAL
    MISTRAL -->|Patches| API
    
    API <--> REDIS
    API <--> SQLITE
```

---

## Comparison Matrix

| Feature | Automated Scanners | Manual Expert Audit | **AccessLens** |
| :--- | :---: | :---: | :---: |
| **Logic Scans (ARIA/DOM)** | Yes | Yes | Yes |
| **Visual Validation** | No | Yes | **Yes (Computer Vision)** |
| **Contextual Awareness** | No | Yes | **Yes (AI Reasoning)** |
| **Automated Remediation** | No | No | **Yes (Synthesized)** |
| **Spatial HUD Mapping** | No | No | **Yes (Real-time)** |

---

## Technical Stack

| Category | Technologies |
| :--- | :--- |
| **Frontend** | Next.js 14, Framer Motion, Tailwind CSS v4 |
| **Backend** | FastAPI, Playwright, Axe-Core |
| **Intelligence** | LLaVA, Mistral 7B, Sentence-Transformers |
| **Infrastructure** | Docker, Redis, SQLite |

---

## Documentation

For deep-dive documentation on specific system components, visit the [Documentation Hub](./docs):
- [System Architecture & AI Pipelines](./docs/ARCHITECTURE.md)
- [Frontend Design & HUD Logic](./docs/FRONTEND.md)
- [Backend Engine Specifications](./docs/BACKEND.md)
- [Contributing Guide](./docs/CONTRIBUTING.md)
- [Setup & Deployment](./docs/SETUP.md)
- [**Development Journey & Roadmap**](./DEVELOPMENT.md)

---
##  Live Demo

- Live App: https://accesslens-azure.vercel.app/
- Backend API: https://sansritimishra-accesslens-backend.hf.space/
---
## Quick Start

1. **Clone**: `git clone https://github.com/Upanshi-Mittal/Accesslens`
2. **Launch**: `docker-compose up --build -d`
3. **Analyze**: Access the dashboard at `http://localhost:3000`

---
## Environment Fidelity & Security Sandbox

### Cloud vs. Local Execution
AccessLens performance and reach depend on the network environment:

*   **Cloud Demo (Hugging Face)**: Operates under strict SSRF Security Protocols. Requests to certain high-complexity or internal-cluster domains (e.g., YouTube, HuggingFace.co) may be blocked by cloud-provider firewalls or DNS filters to prevent scraping abuse.
*   **Local Engine (Recommended)**: For full-depth audits of Shadow DOM-heavy sites, run the project locally. The local engine is unthrottled and provides the highest fidelity results.

#### High-Complexity Audit Samples
| Hugging Face (Cloud Analysis) | YouTube (Local Shadow DOM Piercing) |
| :---: | :---: |
| ![Hugging Face Audit](https://github.com/Upanshi-Mittal/Accesslens/blob/main/docs/images/hg.jpeg?raw=true) | ![YouTube Audit](https://github.com/Upanshi-Mittal/Accesslens/blob/main/docs/images/yt.jpeg?raw=true) |

---

### [License](./LICENSE) | [Code of Conduct](./CODE_OF_CONDUCT.md) | [Security](./SECURITY.md)
