# AccessLens Documentation Hub

Welcome to the official documentation for **AccessLens**, a high-performance accessibility auditing platform.

## Documentation Navigation

- **[System Architecture](./ARCHITECTURE.md)**: High-level overview of the decoupled Next.js + FastAPI system.
- **[Backend Design](./BACKEND.md)**: Details on the analysis engines, browser management, and API orchestration.
- **[Frontend Design](./FRONTEND.md)**: Technical guide to the premium HUD dashboard, design system, and visual components.
- **[Setup & Deployment](./SETUP.md)**: Instructions for local development and production deployment.
- **[Contributing Guide](./CONTRIBUTING.md)**: Guidelines for adding engines and testing standards.

> [!NOTE]
> The root `models/` directory is currently optional. It is intended for persistent storage of local model weights (e.g., GGUF files) if the backend is configured to load them directly into memory. In the default configuration, AI models are accessed via REST API endpoints.

## Project Structure

```text
AccessLens/
├── backend/          # FastAPI server, engines, and browser manager
├── frontend/         # Next.js 14 dashboard and UI components
├── docs/             # Centralized documentation (You are here)
├── data/             # Persistent storage (SQLite, screenshots)
└── models/           # AI model storage (LLaVA, Mistral)
```

## Quick Start

For detailed instructions, see **[SETUP.md](./SETUP.md)**.

1. **Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python run.py
   ```

2. **Frontend**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Contribution

AccessLens is designed with a modular engine system. To add a new accessibility check:
1. Implement a new class inheriting from `BaseEngine` in `backend/app/engines/`.
2. Register the engine in the `AuditOrchestrator`.
3. Update the frontend UI to display the new issue categories if necessary.
