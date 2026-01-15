from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="GetAround Price Predictor",
    description="API pour prédire le prix de location journalier d'une voiture."
)

# Chargement du modèle
model = joblib.load('model.joblib')

class PredictionInput(BaseModel):
    input: list

@app.get("/")
def index():
    return {"message": "Bienvenue sur l'API GetAround. Allez sur /docs pour la documentation."}

@app.post("/predict")
def predict(data: PredictionInput):
    # Les colonnes doivent correspondre exactement à l'entraînement
    columns = ['model_key', 'mileage', 'engine_power', 'fuel', 'paint_color', 
               'car_type', 'private_parking_available', 'has_gps', 
               'has_air_conditioning', 'automatic_car', 'has_getaround_connect', 
               'has_speed_regulator', 'winter_tires']
    
    df_input = pd.DataFrame(data.input, columns=columns)
    prediction = model.predict(df_input)
    
    return {"prediction": prediction.tolist()}