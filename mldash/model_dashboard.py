import streamlit as st 
import joblib

# Utilisation de la nouvelle méthode de mise en cache
@st.cache_resource
def load_model():
    return joblib.load('regression.joblib')

st.title('Prévision de prix de maison')

# Entrées utilisateur
taille = st.number_input("Taille de la maison", min_value=0.0, step=1.0)
nb_rooms = st.number_input("Nombre de chambre", min_value=0.0, step=1.0)
garden = st.radio("Il y a un jardin", options=[0, 1], format_func=lambda x: "Oui" if x == 1 else "Non")

# Charger le modèle
model = load_model()

# Validation des entrées
if taille <= 0:
    st.write('Mettre une taille correcte')
if nb_rooms <= 0:
    st.write("Mettre un nombre de chambres correct")

if taille > 0 and nb_rooms > 0:
    # Préparer les données pour la prédiction
    X = [[taille, nb_rooms, garden]]
    prediction = model.predict(X)
    # Afficher la prédiction
    st.write(f"Le prix de la maison est : {prediction[0]:,.2f}")