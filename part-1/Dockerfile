# Use an official Python runtime as a parent image
FROM python:3.10.4-alpine3.15

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the command to start the Flask app
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]
