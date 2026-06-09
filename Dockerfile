# ---------- STAGE 2: Final ----------
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Add local bin to PATH
ENV PATH=/root/.local/bin:$PATH

# Copy project files
COPY . .

# ❌ DO NOT RUN Django commands here

# Run with Gunicorn
CMD ["gunicorn", "djangoproject.wsgi:application", "--bind", "0.0.0.0:8000"]