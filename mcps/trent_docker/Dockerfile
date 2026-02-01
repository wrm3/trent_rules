# trent_docker - Unified MCP Server
# Combines RAG, Research, MediaWiki, and Template Installation

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
# git required for some pip installs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt pyproject.toml ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY trent/ ./trent/
COPY templates/ ./templates/
COPY templates_full/ ./templates_full/

# Create necessary directories
RUN mkdir -p /app/data /app/logs /app/research_output

# Environment variables (can be overridden)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV LOG_LEVEL=INFO

# Expose port for HTTP/SSE transport
EXPOSE 8082

# Default command - stdio transport (for IDE integration)
# Override with docker run command for HTTP transport
CMD ["python", "-m", "trent.server"]
