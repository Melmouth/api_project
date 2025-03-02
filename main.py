from fastapi import FastAPI
from pydantic import BaseModel
from model_functions import model_loader as mlo

app = FastAPI()

class InputPayload(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class OutputPayload(BaseModel):
    prediction: str

@app.get("/")
async def read_root():
    return {"message": "Hello World, this is a reloaded test"}

model = mlo.load_model(model_path='model.pkl')

@app.post("/echo")
async def echo(payload: InputPayload):
    return payload

@app.post("/predict", response_model=OutputPayload)
def send_back_information(payload: InputPayload):
    input = input.dict()
    prediction = model.predict(input['sepal_length'],
                                input['sepal_width'],
                                input['petal_length'],
                                input['petal_width'])
    map_predict_to_label = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    return {'prediction': map_predict_to_label[prediction]}