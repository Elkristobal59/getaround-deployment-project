# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le dossier de travail
WORKDIR /app

# Copier le fichier des dépendances
# Note : J'utilise le nom 'requirement.txt' car c'est celui que tu as créé
COPY requirement.txt .

# Installer les librairies
RUN pip install --no-cache-dir -r requirement.txt

# Copier tout le reste du projet (scripts + modèle + data)
COPY . .

# Lancer l'API sur le port 7860 (le port par défaut de Hugging Face)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]