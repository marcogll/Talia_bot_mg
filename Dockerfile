# Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /talia_bot

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the package contents
COPY bot bot

# Run the bot via the package entrypoint
CMD ["python", "-m", "bot.main"]
