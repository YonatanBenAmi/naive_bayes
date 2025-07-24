FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY container/classifier_logic ./container/classifier_logic


CMD ["uvicorn", "container.classifier_logic.api:app", "--host", "0.0.0.0", "--port", "8001"]
