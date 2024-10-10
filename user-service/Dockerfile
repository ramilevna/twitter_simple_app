# Dockerfile for User Service

# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service code
COPY . .

# Expose the port the service will run on
EXPOSE 5001

# Command to run the service
CMD ["python", "user_service.py"]

