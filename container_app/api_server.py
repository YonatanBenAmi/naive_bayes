from fastapi import FastAPI
from container_app.classes.get_data import GetData
from container_classifier.classifier_logic.classifier import Classifier
from container_app.classes.data_trainer import Trainer

get_data = GetData()
trainer = Trainer()
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

@app.get('/get_trainer')
def get_trainer():
    return trainer.dict_statistics