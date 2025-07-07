# ---------- Base image ----------
FROM python:3.13-slim-bookworm

# ---------- Runtime env ----------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

# ---------- Install deps ----------
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy source ----------
COPY . .

# ---------- Expose & run ----------
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8080"]
