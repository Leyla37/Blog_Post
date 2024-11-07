# Use the official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Bypass time validation temporarily
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get install -y --no-install-recommends tzdata

# Install build dependencies
RUN apt-get update && apt-get install -y gcc build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
