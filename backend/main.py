# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class IrisData(BaseModel):
    features: list

@app.get("/")
def read_root():
    return {"message": "Iris Classifier API"}

@app.post("/predict")
def predict(data: IrisData):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
