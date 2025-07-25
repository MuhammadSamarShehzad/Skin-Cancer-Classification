# Use official Python image
FROM python:3.10.12-slim

# Set working directory
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Upgrade pip, set timeout, and install dependencies
ENV PIP_DEFAULT_TIMEOUT=120 PIP_DISABLE_PIP_VERSION_CHECK=1
RUN python -m pip install --upgrade pip && \
    pip install --retries 5 --default-timeout=120 --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
