from fastapi import FastAPI
from container_classifier.classifier_logic.classifier import Classifier

app = FastAPI()

classifier = Classifier()


@app.post('/classify')
def classify(request:dict):
    result =  classifier.classify_with_stats(request)
    return result
