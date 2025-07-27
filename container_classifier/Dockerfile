FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY container_classifier ./container_classifier

EXPOSE 8001

CMD ["uvicorn", "container_classifier.classifier_logic.api:app", "--host", "0.0.0.0", "--port", "8001"]
