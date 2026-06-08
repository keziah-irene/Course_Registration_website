# ---------- STAGE 1: Builder ----------
FROM python:3.11 AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

# ---------- STAGE 2: Final ----------
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Add local bin to PATH
ENV PATH=/root/.local/bin:$PATH

# Copy project files
COPY . .

# Collect static files (important for Nginx)
RUN python manage.py collectstatic --noinput

# Run with Gunicorn
CMD ["gunicorn", "djangoproject.wsgi:application", "--bind", "0.0.0.0:8000"]