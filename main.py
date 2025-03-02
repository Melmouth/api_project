from fastapi import FastAPI
from pydantic import BaseModel
from model_functions import model_loader as mlo

app = FastAPI()

class InputPayload(BaseModel):
    prod_year: int
    mileage: float
    cylinders: int
    airbags: int
    fuel_cng: bool
    fuel_diesel: bool
    fuel_hybrid: bool
    fuel_hydrogen: bool
    fuel_lpg: bool
    fuel_petrol: bool
    fuel_plugin_hybrid: bool

class OutputPayload(BaseModel):
    prediction: float

@app.get("/")
async def read_root():
    return {"message": "Hello World, this is a reloaded test"}

model = mlo.load_model(model_path='xgb_model.pkl')

@app.post("/echo")
async def echo(payload: InputPayload):
    return payload

@app.post("/predict", response_model=OutputPayload)
def send_back_information(payload: InputPayload):
    input = payload.dict()
    prediction = model.predict([[input['prod_year'],
                                 input['mileage'],
                                 input['cylinders'],
                                 input['airbags'],
                                 input['fuel_cng'],
                                 input['fuel_diesel'],
                                 input['fuel_hybrid'],
                                 input['fuel_hydrogen'],
                                 input['fuel_lpg'],
                                 input['fuel_petrol'],
                                 input['fuel_plugin_hybrid']]])
    return {'prediction': prediction[0]}