from fastapi import FastAPI
from get_data import GetData

get_data = GetData()
app = FastAPI()

@app.get("/")
def read_root():
    return get_data.get_df()