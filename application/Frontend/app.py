import streamlit as st
import requests

st.title("Chat avec Flask")

user_input = st.text_input("Votre message :", "")
send_button = st.button("Envoyer")

if send_button:
    # Envoyer le message à l'API Flask et afficher la réponse
    response = requests.post("http://localhost:5000/predict", json={"question": user_input})
    if response.status_code == 200:
        reply = response.json()
        st.text(reply)
    else:
        st.error("Une erreur est survenue lors de l'envoi du message.")
