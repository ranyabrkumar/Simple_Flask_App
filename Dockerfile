# Use an official Python base image
FROM python:3.10-slim
# Set working directory inside container
WORKDIR /app
# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the Flask app code
COPY app.py .
# Expose the Flask port
EXPOSE 5000
#` Set environment variable for Flask
CMD ["python", "app.py"]

