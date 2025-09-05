FROM ghcr.io/astral-sh/uv:python3.13-trixie

WORKDIR /app

# Copy dependency files and install to system Python
COPY pyproject.toml uv.lock ./
RUN uv pip install --system -r pyproject.toml

# Copy application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run uvicorn directly (installed to system Python)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
