FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create platforms output dir
RUN mkdir -p /data/platforms

ENV PLATFORMS_DIR=/data/platforms
ENV CRAWL_SCHEDULE="0 2 * * 0"
ENV GIT_AUTO_COMMIT=false

CMD ["python", "scheduler.py", "--daemon"]
