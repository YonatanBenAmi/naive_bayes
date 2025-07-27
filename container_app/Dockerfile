FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY container_app ./container_app
COPY data ./data

EXPOSE 8000

CMD ["uvicorn", "container_app.api_server:app", "--host", "0.0.0.0", "--port", "8000"]