# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY calculator_app.py .

#Create persistent Volume
VOLUME ["/history"]

# Set command to run the application
CMD ["python", "calculator_app.py"]
