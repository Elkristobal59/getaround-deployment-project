from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Initialisation de l'API
app = FastAPI(
    title="GetAround Price Predictor",
    description="API pour prédire le prix de location journalier d'une voiture."
)

# --- CONFIGURATION CORS ---
# Indispensable pour que le Dashboard (autre domaine) puisse appeler l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet les requêtes depuis n'importe quel domaine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chargement du modèle (assure-toi que model.joblib est dans le même dossier)
try:
    model = joblib.load('model.joblib')
except Exception as e:
    print(f"Erreur de chargement du modèle : {e}")

# Modèle de données attendu
class PredictionInput(BaseModel):
    input: list  # Liste de listes ou liste de valeurs selon ton entraînement

@app.get("/")
def index():
    return {
        "message": "Bienvenue sur l'API GetAround.",
        "status": "online",
        "documentation": "/docs"
    }

@app.post("/predict")
def predict(data: PredictionInput):
    # Les colonnes doivent correspondre exactement à l'entraînement du modèle
    columns = [
        'model_key', 'mileage', 'engine_power', 'fuel', 'paint_color', 
        'car_type', 'private_parking_available', 'has_gps', 
        'has_air_conditioning', 'automatic_car', 'has_getaround_connect', 
        'has_speed_regulator', 'winter_tires'
    ]
    
    # Transformation de l'input en DataFrame
    df_input = pd.DataFrame(data.input, columns=columns)
    
    # Prédiction
    prediction = model.predict(df_input)
    
    # Retourne le résultat sous forme de liste JSON
    return {"prediction": prediction.tolist()}