# Use the official Python image as a base
FROM python:3.13.1-slim


# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY requirements.txt /app/
COPY /images /app/images

# Install Flask
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port 5000 for the mock backend
EXPOSE 5000

# Set the command to run the mock backend app
CMD ["python", "mock_backend.py"]