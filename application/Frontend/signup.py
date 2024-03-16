import streamlit as st
import requests
from config import URL

def on_signup_button_pressed():
    username = st.session_state['username']
    password = st.session_state['password']

    response = requests.post(URL + "add_user", json={
        'username': username,
        'password': password
    })
    message = response.json().get('message', '')

    if response.status_code == 200:
        st.success(message)
        st.session_state['current_page'] = 'Login'
        st.session_state['signup_pressed'] = True
    else:
        st.error(message)

def on_login_button_pressed():
    st.session_state['current_page'] = 'Login'
    st.session_state['login_pressed'] = True

def show_signup():
    st.title("Signup Page")

    username = st.text_input("Username", key='username')
    password = st.text_input("Password", type="password", key='password')

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        if st.button("S'inscrire", on_click=on_signup_button_pressed):
            pass 

    with col2:
        if st.button("Connexion", on_click=on_login_button_pressed):
            pass
        
if 'login_pressed' in st.session_state and st.session_state['login_pressed']:
    st.session_state['login_pressed'] = False 
