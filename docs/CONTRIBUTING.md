# Contributing to AccessLens

Thank you for contributing to our deterministic and AI-powered accessibility auditor! AccessLens is a full-stack HUD-inspired OS built on a modular "Collective Intelligence" architecture.

---

## Backend Development (Python/FastAPI)

All analysis logic is encapsulated in engines. To add a new check:

### 1. Implement the Engine Interface
Create a new file in `backend/app/engines/your_engine.py`:
- Inherit from `BaseAccessibilityEngine`.
- Return a list of `UnifiedIssue` objects.

### 2. Register Your Engine
Add your engine instance to the registry in `backend/app/core/dependencies.py`.

---

## Frontend Development (Next.js/Tailwind)

Our frontend is a high-performance HUD designed for visual density and technical clarity.

### 1. Technology Stack
- **Framework**: Next.js 14 (App Router).
- **Styling**: Tailwind CSS v4 (Vanilla CSS variables).
- **Animation**: Framer Motion (use for all transitions and micro-interactions).
- **Icons**: Lucide React (always use for consistent symbolism).

### 2. Design Code of Conduct
- **Premium HUD Aesthetic**: Use glassmorphism (`backdrop-blur-3xl`), subtle gradients, and technical borders.
- **Micro-Animations**: All interactive elements (buttons, cards) must have hover/active states.
- **Typography**: Adhere strictly to the `Roboto Mono` and monospace font scales for a terminal-like feel.

---

## Testing Strategy

We maintain a strict tiered testing approach to balance speed and coverage.

### 1. Unit Tests
- **Backend**: `pytest backend/tests/ -m unit`
- **Frontend**: Standard Vitest/Jest suite (if applicable).

### 2. Browser Integration Tests (Playwright)
- Tests that launch physical browser instances to verify engine and UI accuracy.
- Execution: `pytest backend/tests/ -m browser`

---

## Development Standards

- **Code Style**: PEP8 for Python; Prettier/ESLint for Next.js.
- **Async First**: Use `async/await` for all I/O and browser operations.
- **Type Safety**: New components MUST include Pydantic models (backend) or TypeScript interfaces (frontend).

---
*Built with precision for the modern web.*
