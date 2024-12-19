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

def test_model_basic(train_data):
    """Test l'entraînement et les prédictions basiques"""
    X, y = train_data
    model = LinearRegression()
    model.fit(X, y)
    
    # Vérifie l'entraînement et la performance
    assert hasattr(model, 'coef_')
    assert model.score(X, y) > 0.15

def test_price_logic(model):
    """Test que le modèle respecte la logique immobilière de base"""
    # Petite maison
    small_house = pd.DataFrame({
        'size': [85],
        'nb_rooms': [2],
        'garden': [0]
    })
    
    # Grande maison
    large_house = pd.DataFrame({
        'size': [205],
        'nb_rooms': [2],
        'garden': [0]
    })
    
    # Même maison avec jardin
    house_with_garden = pd.DataFrame({
        'size': [85],
        'nb_rooms': [2],
        'garden': [1]
    })
    
    # Tests logiques
    small_price = model.predict(small_house)[0]
    large_price = model.predict(large_house)[0]
    garden_price = model.predict(house_with_garden)[0]
    
    assert large_price > small_price  # plus grand = plus cher
    assert garden_price > small_price  # jardin = plus cher
    
    # Prix min observé (hors négatifs) : ~222,231€
    # Prix max observé : ~333,781€
    assert 222_000 <= small_price <= 334_000  # prix réalistes