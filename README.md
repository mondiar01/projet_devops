# projet_devops
Dans ce projet on veut mettre en place une pipeline qui permet de tester automatiquement un modèle intégré à un petit tableau de bord. Le tableau de bord a été codé et est disponible ici : https://github.com/lcetinsoy/mldash

# Prédiction de Prix de Maisons 🏠

Une application de Machine Learning déployée avec Streamlit pour prédire les prix des maisons.

## 📌 Table des Matières
- [Aperçu](#aperçu)
- [Architecture](#architecture)
- [Installation](#installation)
- [Tests](#tests)
- [Déploiement](#déploiement)
- [CI/CD](#cicd)

## 🎯 Aperçu

Cette application utilise un modèle de Machine Learning pour prédire le prix des maisons en se basant sur différentes caractéristiques.


![Page d'accueil de l'application Streamlit](/docs/images/page_accueil_app_streamlit.png)

### Fonctionnalités principales:
- Prédiction en temps réel des prix
- Interface utilisateur intuitive
- Visualisation des données
- API REST pour les intégrations

## 🏗 Architecture

```plaintext
project_devops/
├── mldash/
│   ├── app.py            # Application Streamlit
│   └── model.py
│   └── __init__.py
│   └── houses.csv    
├── tests/
│   └── conftest.py
│   └── test_model.py     # Tests unitaires
│   └── __init__.py
├── Dockerfile
└── requirements.txt
└── requirements_tests.txt
```

## 💻 Installation

1. Cloner le repository:
```bash
git clone [URL_DU_REPO]
cd house-prediction
```

2. Créer un environnement virtuel:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. Installer les dépendances:
```bash
pip install -r requirements.txt
```

4. Lancer l'application:
```bash
streamlit run app/app.py
```

![Application en local avec des exemples de prédictions](/docs/images/exemple_de_prediction_local.png)

## 🧪 Tests

Exécuter les tests:
```bash
pytest tests/test_model.py
```

[CAPTURE ÉCRAN 3: ]
![Résultats des tests](docs/images/resultats_test.png)
## 🚀 Déploiement

### Avec Docker:
```bash
docker build -t houses-prediction .
docker run -p 8501:8501 houses-prediction
```

[CAPTURE ÉCRAN 4: ]
![Application dockerisée en cours d'exécution](/docs/images/exemple_de_prediction_local.png)
## 🔄 CI/CD

Le projet utilise GitHub Actions pour:
- Exécuter les tests automatiquement
- Générer des rapports de tests
- Builder et pusher l'image Docker
- Déployer automatiquement

[CAPTURE ÉCRAN 5: Pipeline GitHub Actions réussi]

### Configuration requise pour le CI/CD:

1. Secrets GitHub nécessaires:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`

2. Docker Hub Token:
   - Générer depuis Docker Hub (Security > Access Tokens)
   - Configurer avec les permissions Read & Write

[CAPTURE ÉCRAN 6:]
![ Configuration des secrets GitHub](/docs/images/exemple_de_prediction_local.png)
## 📊 Performances du Modèle

[CAPTURE ÉCRAN 7: ]
![Métriques du modèle et graphiques de performance](/docs/images/exemple_de_prediction_local.png)
## 🛠 Stack Technique

- Python 3.10
- Streamlit
- FastAPI
- scikit-learn
- Docker
- GitHub Actions

## 📫 Contact

Modou Ndiar DIA - diamodoundiar@gmail.com


