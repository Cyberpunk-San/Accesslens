# Setup & Deployment Guide

This guide provides step-by-step instructions for setting up the AccessLens platform in development and production environments.

## Prerequisites

- **Python**: 3.10 or higher
- **Node.js**: 18.x or higher
- **Playwright**: Installed via `playwright install`
- **SQLite**: (Built-in to Python)

---

## 1. Backend Setup

The backend handles audit orchestration, browser management, and engine analysis.

1. **Clone the repository and enter the backend directory**:
   ```bash
   cd AccessLens/backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

4. **Configuration**:
   Copy `.env.example` to `.env` and adjust settings (database URL, API keys for AI, etc.).

5. **Run the server**:
   ```bash
   python run.py
   ```
   The backend will be available at `http://localhost:8000`.

> [!TIP]
> **AI Models**: By default, AccessLens connects to LLaVA and Mistral via API endpoints. If you wish to use local weights instead:
> 1. Download the GGUF/Safetensors weights to the root `models/` directory.
> 2. Set `AI_USE_LOCAL=True` and configure the appropriate paths in your `.env`.

---

## 2. Frontend Setup

The frontend is a Next.js application for visualizing audit results.

1. **Enter the frontend directory**:
   ```bash
   cd AccessLens/frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configuration**:
   Ensure `.env.local` points to the correct backend API:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```
   The dashboard will be available at `http://localhost:3000`.

---

## 3. Production Deployment (Docker)

AccessLens uses a root-level `docker-compose.yml` for unified orchestration of the frontend, backend, and Redis services.

1. **Build and start all services**:
   ```bash
   # From the project root
   docker-compose up --build -d
   ```

2. **Access the platform**:
   - Dashboard: `http://localhost:3000`
   - Backend API: `http://localhost:8000/api/v1`

3. **Check logs**:
   ```bash
   docker-compose logs -f
   ```

---

## 4. Troubleshooting

- **Browser Crashes**: Ensure `playwright install chromium` was successful and that your environment has the necessary libraries for headless browsers.
- **Database Errors**: If `accesslens.db` becomes corrupted or needs a reset, delete the file and restart the backend; it will automatically recreate the schema.
- **Port Conflicts**: If ports 3000 or 8000 are occupied, adjust the `docker-compose.yml` or your local environment variables.
