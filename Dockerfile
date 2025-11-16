# Use an official Python runtime as a parent image
FROM python:3.13.5-slim-bookworm



# Set the working directory in the container
WORKDIR /app

# Install uv for package management from latest uv image into /bin/uv in this image , uv is fast Python package installer and environment manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the dependency file
COPY pyproject.toml ./
COPY README.md .
# Add virtual environment's bin directory to the PATH so Python tools work globally
ENV PATH="/APP/.venv/bin:$PATH"

# Copy the dependency file UV.LOCK AND PYTHON VERSION 
COPY "pyproject.toml"   ./

##RUN uv sync --locked

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
