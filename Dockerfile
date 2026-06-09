# ---------- STAGE 1: Builder ----------
FROM python:3.11 AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

# ---------- STAGE 2: Final ----------
FROM python:3.11-slim

WORKDIR /app

# MUST match "builder"
COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

COPY . .

CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn djangoproject.wsgi:application --bind 0.0.0.0:8000"]
