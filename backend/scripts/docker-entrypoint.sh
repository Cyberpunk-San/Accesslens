#!/bin/bash
set -e

# Create necessary directories if they don't exist
mkdir -p /app/data /app/models /app/logs

# Initialize the database if it doesn't exist
if [ ! -f "/app/data/accesslens.db" ]; then
    echo "Initializing SQLite database..."
    python scripts/setup_db.py
fi

# Run any pending migrations (if the script exists and is configured)
if [ -f "scripts/run_migrations.py" ]; then
    echo "Running database migrations..."
    python scripts/run_migrations.py
fi

# Execute the given command (usually uvicorn)
echo "Starting AccessLens API..."
exec "$@"
