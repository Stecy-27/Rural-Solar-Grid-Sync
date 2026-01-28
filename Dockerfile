FROM python:3.11-alpine

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .
COPY data/ ./data

EXPOSE 5000

CMD ["python", "main.py"]
