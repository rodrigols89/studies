# ===============================
# Base image
# ===============================
FROM python:3.12-slim

# ===============================
# System dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    iputils-ping \
    bash \
    gosu \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Create appuser
# ===============================
RUN useradd \
    --create-home \
    --shell /bin/bash \
    --uid 1000 \
    appuser

# ===============================
# Set workdir
# ===============================
WORKDIR /code

# ===============================
# Set environment variables
# ===============================
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/code \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/home/appuser/.local/bin:$PATH"

# ===============================
# Install poetry
# ===============================
RUN pip install --upgrade pip && pip install poetry

# ===============================
# Copy dependencies
# ===============================
COPY pyproject.toml poetry.lock /code/

# ===============================
# Install dependencies
# ===============================
RUN poetry install --no-root --no-interaction --no-ansi

# ===============================
# Copy the code (project)
# ===============================
COPY . /code/

# ===============================
# Copy entrypoint script
# ===============================
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ===============================
# Set initial script
# ===============================
ENTRYPOINT ["/entrypoint.sh"]
