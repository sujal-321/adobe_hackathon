 # Use a lightweight Python image for AMD64 architecture
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script
COPY challenge_1.py .

# Set the default command to run your script
ENTRYPOINT ["python", "challenge_1.py"]

