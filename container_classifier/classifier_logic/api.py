from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from container_classifier.classifier_logic.classifier import Classifier

app = FastAPI()
classifier = Classifier()

class ClassifyRequest(BaseModel):
    data: Dict[str, str]  # תתאם לסוג של הקלט שלך

@app.post("/classify")
def classify(request: ClassifyRequest):
    print("Received request:", request)
    result = classifier.classify_with_stats(request.data)
    return result

@app.get("/")
def healthcheck():
    return {"status": "ok"}
