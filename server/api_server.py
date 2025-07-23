from fastapi import FastAPI
from server.classes.get_data import GetData
from server.classes.classifier import Classifier
from server.classes.data_trainer import Trainer

get_data = GetData()
trainer = Trainer()
classifier = Classifier(trainer)
app = FastAPI()


@app.get("/")
def read_root():
    return get_data.get_df()

@app.get("/uniqe_val")
def dict_uniqe_val() -> dict:
    return get_data.get_dict_unique_val()

@app.get("/last_column")
def last_column() -> list:
    return get_data.get_last_colomn()

@app.get("/other_column")
def other_column() -> list:
    return get_data.get_other_columns()

@app.post('/classify')
def classify(request:dict):
    result =  classifier.classify_with_stats(request)
    return result



