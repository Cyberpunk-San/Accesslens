# AccessLens Documentation Hub

Welcome to the official documentation for **AccessLens**,accessibility auditing platform.

## Documentation Navigation

- **[System Architecture](./ARCHITECTURE.md)**: overview of the Next.js + FastAPI system.
- **[Backend Design](./BACKEND.md)**: Details on the analysis engines, browser management, and API orchestration.
- **[Frontend Design](./FRONTEND.md)**: Technical guide to the HUD dashboard, design system, and visual components.
- **[Setup & Deployment](./SETUP.md)**: Instructions for local development and production deployment.
- **[Contributing Guide](./CONTRIBUTING.md)**: Guidelines for adding engines and testing standards.

## Project Structure

```text
AccessLens/
├── backend/          # FastAPI server, engines, and browser manager
├── frontend/         # Next.js 14 dashboard and UI components
├── docs/             # Centralized documentation (You are here)
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
