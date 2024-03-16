import streamlit as st
import requests
from config import URL

def on_login_button_pressed():
    username = st.session_state['username']
    password = st.session_state['password']

    response = requests.post(URL + "/login", json={
        'username': username,
        'password': password
    })
    message = response.json().get('message', '')

    if response.status_code == 200:
        st.session_state['current_page'] = 'Chatbot'
        st.session_state['login_pressed'] = True
        st.session_state['username'] = username
    elif response.status_code == 401:
        st.error(message)
    elif response.status_code == 404:
        st.error(message)
    else:
        st.error("Une erreur s'est produite lors de la tentative de connexion.")


def on_signup_button_pressed():
    st.session_state['current_page'] = 'Signup'
    st.session_state['signup_pressed'] = True

def show_login():
    st.title("Login Page")
    username = st.text_input("Username", key='username')
    password = st.text_input("Password", type="password", key='password')

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        if st.button("Connexion", on_click=on_login_button_pressed):
            pass

    with col2:
        if st.button("Inscription", on_click=on_signup_button_pressed):
            pass  
        
if 'login_pressed' in st.session_state and st.session_state['login_pressed']:
    st.session_state['login_pressed'] = False 

if 'signup_pressed' in st.session_state and st.session_state['signup_pressed']:
    st.session_state['signup_pressed'] = False 