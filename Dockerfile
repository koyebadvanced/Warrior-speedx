FROM python:3.10-slim

# Use apt-get & avoid upgrade
RUN apt-get update && apt-get install -y git && apt-get clean

# Copy requirements and install Python packages
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /requirements.txt

# Set working directory
WORKDIR /VJ-Forward-Bot

# Copy entire codebase to container
COPY . .

# Run both gunicorn and main.py
CMD ["sh", "-c", "gunicorn app:app & python3 main.py"]