FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Install all dependencies in one layer to stay cached
# Using --prefer-binary speeds up torch/transformers by avoiding source builds
RUN pip install --default-timeout=5000 --no-cache-dir --prefer-binary \
    torch transformers accelerate sentencepiece Pillow numpy \
    -r requirements.txt
RUN playwright install chromium

COPY . .

RUN mkdir -p data models

EXPOSE 8000

COPY scripts/docker-entrypoint.sh /usr/local/bin/
RUN sed -i 's/\r$//' /usr/local/bin/docker-entrypoint.sh && \
    chmod +x /usr/local/bin/docker-entrypoint.sh

ENV PYTHONPATH=/app
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]