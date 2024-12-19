import streamlit as st
from model import build_model, predict_price

# Titre de l'application
st.title('Prévision de prix de maison')

# Entraîner le modèle automatiquement si nécessaire
if build_model():
    st.success("Modèle entraîné automatiquement et sauvegardé.")
else:
    st.info("Modèle déjà entraîné.")

# Entrées utilisateur
taille = st.number_input("Taille de la maison (en m²)", min_value=0.0, step=1.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, step=1)
garden = st.radio("Y a-t-il un jardin ?", options=[0, 1], format_func=lambda x: "Oui" if x == 1 else "Non")

# Effectuer la prédiction
if taille > 0 and nb_rooms > 0:
    prediction = predict_price(taille, nb_rooms, garden)
    st.write(f"Le prix prédit de la maison est : {prediction:,.2f} €")
else:
    st.warning("Veuillez entrer des valeurs valides pour effectuer une prédiction.")