import pandas as pd

def test_model_basic(train_data):
    """Test l'entraînement et les prédictions basiques"""
    X, y = train_data
    from sklearn.linear_model import LinearRegression
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
    assert 222_000 <= small_price <= 334_000  # prix réalistes