import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
import numpy as np

def build_model():
    model_path = os.path.join(os.path.dirname(__file__), 'regression.joblib')
    data_path = os.path.join(os.path.dirname(__file__), 'houses.csv')
    
    if not os.path.exists(model_path):
        try:
            df = pd.read_csv(data_path)
            # Créer un DataFrame avec les bonnes colonnes
            X = pd.DataFrame(df[['size', 'nb_rooms', 'garden']])
            y = df['price']
            
            model = LinearRegression()
            model.fit(X, y)
            
            joblib.dump(model, model_path)
            return True
        except Exception as e:
            print(f"Error: {e}")
            print(f"Current directory: {os.getcwd()}")
            print(f"Files in directory: {os.listdir('.')}")
            return False
    return False

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'regression.joblib')
    return joblib.load(model_path)

def predict_price(size, nb_rooms, garden):
    model = load_model()
    # Créer un DataFrame avec les mêmes noms de colonnes que lors de l'entraînement
    X_pred = pd.DataFrame([[size, nb_rooms, garden]], 
                         columns=['size', 'nb_rooms', 'garden'])
    return model.predict(X_pred)[0]