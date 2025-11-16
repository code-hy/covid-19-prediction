# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install uv for package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the dependency file
COPY pyproject.toml ./
COPY README.md .

# Install dependencies
# --system is used because we are not inside a virtual environment in the docker container
RUN uv pip install --system -e .

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# Use 0.0.0.0 to make it accessible from outside the container
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]