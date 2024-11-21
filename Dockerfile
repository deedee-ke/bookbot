# Use the official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install any dependencies (not needed for this example)
# RUN pip install -r requirements.txt

# Set the default command to run the script
CMD ["python", "main.py"]
