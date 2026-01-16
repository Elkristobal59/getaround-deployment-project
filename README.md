# 🚗 Getaround Decision Support System - Christopher GILLERON

Ce projet a été réalisé dans le cadre de la certification **Concepteur et Développeur en Science des Données** chez **JEDHA**. 

L'objectif est de fournir à **Getaround** une solution complète pour gérer les frictions opérationnelles (retards) et optimiser la stratégie de tarification via le Machine Learning.

---

## 🎯 Objectifs du Projet

1.  **Analyse des retards :** Évaluer l'impact des retards de restitution et recommander un seuil de sécurité (buffer) entre deux locations.
2.  **Pricing Engine :** Développer un modèle de Machine Learning prédisant le prix de location journalier optimal.
3.  **Déploiement Industriel :** Mise en production d'un Dashboard décisionnel et d'une API de production.

---

## 🏗️ Architecture du Projet

L'écosystème repose sur deux composants distincts et interconnectés, déployés sur **Hugging Face Spaces** :

### 📊 1. Dashboard d'Analyse (Streamlit)
Outil destiné aux Product Managers pour piloter la politique de "seuil de sécurité".
* **Fonctionnalités :** Visualisation des distributions, analyse Connect vs Mobile, et simulateur d'efficacité du buffer.
* **Lien :** [Accéder au Dashboard](https://huggingface.co/spaces/Elkristobal59/getaround-dashboard) *(Vérifie ton URL exacte)*

### ⚡ 2. API de Prédiction (FastAPI)
Interface technique permettant d'intégrer les prédictions de prix dans n'importe quelle application tierce.
* **Documentation interactive (Swagger) :** [https://elkristobal59-getaround-pricing-api.hf.space/docs](https://elkristobal59-getaround-pricing-api.hf.space/docs)
* **Endpoint :** `POST /predict`

---

## 🧠 Machine Learning & Data Science

### Modèle de Prédiction
* **Algorithme :** Régression (RandomForestRegressor(n_estimators=100, random_state=42)) entraînée sur un dataset de caractéristiques techniques.
* **Features (13) :** Marque, kilométrage, puissance moteur, type de carburant, couleur, type de véhicule, et options (GPS, Clim, Connect, etc.).
* **Pipeline de données :** * **Preprocessing :** Standardisation des données numériques (`StandardScaler`) et encodage des variables catégorielles (`OneHotEncoder`).
* **Gestion des Outliers :** Nettoyage des valeurs extrêmes sur les retards (> 12h) pour garantir la fiabilité des analyses statistiques.



### Insights Business Clés
* **Retards :** Environ **44%** des locations subissent un retard. 
* **Technologie :** Le système **Connect** offre une meilleure régularité de restitution que le système **Mobile**.
* **Recommandation :** L'application d'un seuil de **120 minutes** entre deux locations permet d'absorber la majorité des retards sans impacter drastiquement le volume de réservations.

---
## 🚀 Installation & Utilisation locale

1. **Cloner le projet :**
   ```bash
   git clone [https://github.com/Elkristobal59/getaround-deployment-project.git](https://github.com/Elkristobal59/getaround-deployment-project.git)
Installer les dépendances :

Bash

pip install -r requirements.txt
Lancer le Dashboard :

Bash

streamlit run streamlit_app.py
Lancer l'API :

Bash

uvicorn app:app --reload
🛠️ Stack Technique
Langage : Python (Pandas, Scikit-Learn, Joblib)

Dashboard : Streamlit

API : FastAPI & Pydantic

Visualisation : Plotly Express

Déploiement : GitHub, Hugging Face Spaces, Git LFS


---
