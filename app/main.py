from typing import List

import mlflow.sklearn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = mlflow.sklearn.load_model("model")


class PredictRequest(BaseModel):
    features: List[List[float]]


@app.post("/predict")
def predict(request: PredictRequest):
    predictions = model.predict(request.features)
    return {"predictions": predictions.tolist()}