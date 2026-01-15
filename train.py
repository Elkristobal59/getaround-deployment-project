import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Chargement
df = pd.read_csv('get_around_pricing_project.csv').drop(columns=['Unnamed: 0'])

# Features
X = df.drop(columns=['rental_price_per_day'])
y = df['rental_price_per_day']

# Preprocessing
numeric_features = ['mileage', 'engine_power']
categorical_features = ['model_key', 'fuel', 'paint_color', 'car_type']
binary_features = ['private_parking_available', 'has_gps', 'has_air_conditioning', 
                   'automatic_car', 'has_getaround_connect', 'has_speed_regulator', 'winter_tires']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ('bin', 'passthrough', binary_features)
    ])

# Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Training
model.fit(X, y)

# Sauvegarde
joblib.dump(model, 'model.joblib')