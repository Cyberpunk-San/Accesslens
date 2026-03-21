# AccessLens Frontend: The Cyber-HUD Architecture

The AccessLens frontend is a high-performance, **Intelligence Hub** built with **Next.js 14**. It is designed with a "Cyber-HUD" (Heads-Up Display) aesthetic, prioritizing technical density, visual depth, and real-time feedback.

---

## Technical Stack

- **Framework**: Next.js 14 (App Router)
- **Styling**: Tailwind CSS v4 (Full CSS-variable integration)
- **Animations**: Framer Motion (Orchestrating all layout transitions and HUD micro-interactions)
- **Visual Effects**: Vanilla Canvas + CSS (Matrix Rain, Scanning Shaders)
- **State & Data**: TanStack React Query + Custom Hooks
- **Icons**: Lucide React (Symbolic consistency)

---

## Design System: The Cyber-HUD Aesthetic

AccessLens follows a strict "Technical UI" language, designed to feel like an advanced operating system rather than a traditional website.

### 1. The Matrix Foundation
The application uses a **MatrixRain** canvas background to provide low-distraction visual motion, reinforcing the "Digital Intelligence" theme. This is implemented via a high-performance Canvas element with custom glyph-streaming logic.

### 2. HUD Fragments & Clippings
Interactive elements use **Cyber-Hex** and **Clipped Corner** patterns:
- **Glassmorphism**: 1px translucent borders (`white/10`) with heavy `backdrop-blur-3xl`.
- **Adaptive HUD Borders**: Containers often feature "Tech Corner" accents—floating L-shaped borders that highlight active focus zones.
- **Floating HUD Elements**: The `AuditLoading` component uses floating data fragments and sweeping scan-lines to communicate background processing state.

### 3. Typography & Symbolism
- **Primary Type**: Monospace (`Roboto Mono` / `Courier New`) for technical data and headers.
- **Functional Icons**: Precise Lucide icons used for "Intelligence Summary," "Spatial Map," and "Remediation Strategy."

---

## Core Views & Components

### 1. The HUD Dashboard (`/dashboard`)
The central command center. Focused on high-level executive metrics:
- **Audit Pulse**: A visual record of scan frequency.
- **Severity Heatmap**: A color-coded distribution of critical vs. moderate barriers.

### 2. The Remediation Hub (`/audit/[id]`)
Where structural data meets AI intelligence.
- **The Issue Matrix**: A filterable HUD list of violations.
- **The Intelligence Layer**: Executive summaries synthesized from engine output.
- **Remediation Strategy**: Side-by-side **Synthetic Code Patches**—AI-generated diffs showing the exact code fix required.
- **Heatmap Overlay**: A 1:1 spatial mapping system that "pings" violations directly onto the page screenshot.
- **Tree Visualizer**: An interactive explorer for the Accessibility Tree (AX Tree).

---

## Performance Patterns

- **Standalone Optimization**: The frontend is built for **Next.js Standalone mode**, significantly reducing Docker image size and cold-start times.
- **Hydration Guards**: Specialized logic for Matrix and HUD effects to ensure smooth SSR-to-Client transitions.
- **Optimistic HUD**: Immediate UI feedback for new audit submissions before background analysis completes.

---
*Built for the next generation of digital accessibility.*
