# Use base image
FROM python:3.12.2-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies and clean up to reduce image size
RUN apt-get update && apt-get install -y netcat-traditional gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only requirements file to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Ensure entrypoint script is executable
RUN chmod +x ./docker/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Run the entrypoint script to start the Django app
ENTRYPOINT ["./docker/entrypoint.sh"]
