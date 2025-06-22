from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

class IrisData(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Welcome to Iris ML API on Hugging Face!"}

@app.post("/predict")
def predict(data: IrisData):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
