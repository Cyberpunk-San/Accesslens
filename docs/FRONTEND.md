# AccessLens Frontend Architecture

The AccessLens frontend is a high-performance, premium dashboard built with **Next.js 14**, utilizing the **App Router** and a HUD-inspired design system.

## Core Technologies

- **Framework**: Next.js 14 (App Router)
- **Styling**: Tailwind CSS v4 (Alpha/Edge) + CSS Variables
- **State Management**: TanStack React Query (Server/Client state synchronization)
- **Animations**: Framer Motion (Smooth layout transitions and micro-interactions)
- **Icons**: Lucide React
- **Typography**: Inter (Body), Outfit (Headings)

## Visual Architecture

The UI is designed to feel like a "Command Center" or "Digital Intelligence Hub," prioritizing dark aesthetics, glassmorphism, and glowing elements.

### 1. Intelligence Dashboard (`/dashboard`)
- Provides a high-level summary of recent audit activity.
- Visual components for audit frequency, severity distribution, and average compliance scores.

### 2. Audit Results (`/audit/[id]`)
The core analysis view, split into specialized tabs:

- **Issue Matrix**: A detailed list of all detected barriers, categorized by severity and engine source.
- **Spatial Map (Heatmap)**: An interactive overlay that maps issues directly onto the target page's screenshot.
- **Tree Map**: A hierarchical "Digital Architecture" explorer for the Accessibility Tree (AX Tree).
- **Intelligence (Analytics)**: High-level executive synthesis and engine-specific breakdowns.

## Key Components

- `IntelligenceSummary.tsx`: Synthesizes raw audit data into a readable technical briefing.
- `HeatmapOverlay.tsx`: Manages the spatial coordinate mapping and "ping" animations for issues.
- `TreeVisualizer.tsx`: Recursively renders the AX tree with search and a dedicated "Node Inspector."
- `AuditLoading.tsx`: A premium "Cyber-Scan" animation for wait states.
- `AuditMeditation.tsx`: A tranquil wait-state for longer data syntheses.

## Design System

The design system is defined primarily through tailored CSS variables in `globals.css` and a custom theme block in `tailwind.config.js`.

- **Colors**:
  - `brand`: Deep Indigo/Violet primary.
  - `slate`: Technical neutral for borders/secondary text.
  - `rose`: Critical severity signals.
  - `amber`: Serious/Moderate warnings.
- **Glassmorphism**: Extensive use of `backdrop-blur` and low-opacity borders (`white/5`) to create depth.
- **Glow Effects**: Precise `box-shadow` and `filter: drop-shadow` utilities for high-end visual feedback.

## Data Fetching Pattern

AccessLens uses custom hooks (`src/hooks/use-audits.ts`) that wrap `useQuery`. This ensures:
- Automatic caching and revalidation of audit results.
- Robust loading/error states integrated with the `AuditLoading` and `AuditMeditation` components.
- Optimistic updates for new audit submissions.
