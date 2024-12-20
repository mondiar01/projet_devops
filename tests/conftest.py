import pytest
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

@pytest.fixture
def train_data():
    data_path = os.path.join(os.path.dirname(__file__), '../mldash/houses.csv')
    """Prépare les données d'entraînement"""
    df = pd.read_csv(data_path)
    # Filtrer les prix négatifs qui sont probablement des erreurs
    df = df[df['price'] > 0]
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    return X, y

@pytest.fixture
def model(train_data):
    """Crée et entraîne le modèle"""
    X, y = train_data
    model = LinearRegression()
    model.fit(X, y)
    return model