# Use slim Python image
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY app/ .

# Expose the runtime port
ENV PORT 8080
EXPOSE 8080

# Launch the app
CMD ["python", "main.py"]
