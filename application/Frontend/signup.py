import streamlit as st
import requests
from Ressources.Config import URL


def view_signup():
    st.title("Signup Page")
    st.write("You don't have an account yet? Please signup. If you already have an account, please login.")

    username = st.text_input("Username", key='username')
    password = st.text_input("Password", type="password", key='password')

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        signup_disabled = not username or not password
        if st.button("Signup", on_click=function_signup_button_pressed, disabled=signup_disabled):
            pass 

    with col8:
        if st.button("Login", on_click=function_login_button_pressed):
            pass


def function_signup_button_pressed():
    response = requests.post(URL + "signup", json={
        'username': st.session_state['username'],
        'password': st.session_state['password']
    })
    message = response.json().get('message', '')

    if response.status_code == 200:
        st.success(message)
        st.session_state['current_page'] = 'Login'
        st.session_state['signup_pressed'] = True
        st.session_state['username'] = None
        st.session_state['password'] = None
    else:
        st.error(message)


def function_login_button_pressed():
    st.session_state['current_page'] = 'Login'
    st.session_state['login_pressed'] = True