FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir dockerfile-parse

CMD ["python", "analyze_dockerfile.py"]
