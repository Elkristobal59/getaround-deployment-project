# 🚗 Projet Getaround - Christopher GILLERON

Ce projet a été réalisé par **Christopher GILLERON** dans le cadre de la formation **Concepteur et Développeur en Science des Données** suivie chez **JEDHA**. 

L'objectif est d'accompagner l'entreprise Getaround dans l'amélioration de son expérience utilisateur et l'optimisation des revenus des propriétaires via l'analyse de données et le Machine Learning.

## 🎯 Objectifs du Projet
1. **Analyse des retards :** Déterminer l'impact des retards de restitution sur les locations suivantes et suggérer un seuil de sécurité (buffer) entre deux réservations.
2. **Optimisation des prix :** Créer un modèle de Machine Learning capable de suggérer un prix de location journalier optimal pour les propriétaires.
3. **Déploiement :** Mettre à disposition un Dashboard interactif pour les décisions business et une API de prédiction pour l'intégration technique.

---

## 📊 1. Dashboard d'Analyse (Streamlit)
Le dashboard permet au Product Manager d'explorer les données de retard et de simuler l'impact d'un délai minimum entre deux locations.

* **Lien du Dashboard :** [INSERE_ICI_TON_URL_STREAMLIT_HUGGING_FACE]
* **Insights clés :** * Environ **52%** des utilisateurs restituent leur véhicule en retard.
    * Les voitures équipées de la technologie **Connect** présentent des retards moins fréquents que celles sous contrat **Mobile**.
    * Un seuil de **120 minutes** est recommandé pour régler la majorité des collisions critiques.

---

## ⚡ 2. API de Prédiction (FastAPI)
L'API permet d'interroger notre modèle de Machine Learning pour obtenir une suggestion de prix en temps réel basée sur les caractéristiques du véhicule.

* **Documentation interactive (Swagger) :** [INSERE_ICI_TON_URL_API_HUGGING_FACE]/docs
* **Endpoint :** `POST /predict`

### Exemple de requête avec cURL :
```bash
curl -i -H "Content-Type: application/json" \
     -X POST \
     -d '{"input": [["Citroën", 140411, 100, "diesel", "black", "convertible", true, true, false, false, true, true, true]]}' \
     https://[TON_URL_API]/predict
