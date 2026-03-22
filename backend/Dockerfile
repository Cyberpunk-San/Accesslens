# Stage 1: Build dependencies
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install dependencies into a specific directory for easy copying
RUN pip install --no-cache-dir --prefix=/install --prefer-binary \
    torch transformers accelerate sentencepiece Pillow numpy \
    -r requirements.txt

# Stage 2: Runtime
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app
ENV PYTHONPATH=$APP_HOME

WORKDIR $APP_HOME

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Install chromium (Playwright specific)
RUN playwright install chromium

# Copy application code
COPY . .

RUN mkdir -p data models logs

EXPOSE 8000

COPY scripts/docker-entrypoint.sh /usr/local/bin/
RUN sed -i 's/\r$//' /usr/local/bin/docker-entrypoint.sh && \
    chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]