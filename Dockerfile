# Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /talia_bot

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY talia_bot/ .

# Run the bot
CMD ["python", "main.py"]
