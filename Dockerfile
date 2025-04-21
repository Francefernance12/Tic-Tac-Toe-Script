# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /Tic-Tac_Toe

# Copy all files to the container
COPY . /Tic-Tac_Toe

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV PYTHONPATH=/Tic-Tac_Toe

# Run the application
CMD ["python", "main.py"]