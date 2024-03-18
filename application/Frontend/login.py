import streamlit as st
import requests
from Ressources.Config import URL


def view_login():
    st.title("Login Page")
    
    st.text_input("Username", key='username')
    st.text_input("Password", type="password", key='password')

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        if st.button("Login", on_click=function_login_button_pressed):
            pass

    with col8:
        if st.button("Signup", on_click=function_signup_button_pressed):
            pass  
        

def function_login_button_pressed():
    response = requests.post(URL + "/login", json={
        'username': st.session_state['username'],
        'password': st.session_state['password']
    })

    content = response.json()
        
    if response.status_code == 200:
        st.session_state['current_page'] = 'Chatbot'
        st.session_state['login_pressed'] = True

        st.session_state['user_id'] = content['user_id']
        st.session_state['user_name'] = content['user_name']
        st.session_state['user_is_connected'] = content['user_is_connected']

        st.session_state['username'] = None
        st.session_state['password'] = None
        
    elif response.status_code == 401:
        st.error(content['message'])
    elif response.status_code == 404:
        st.error(content['message'])
    else:
        st.error("Error: 500 Internal Server Error. Please try again later.")


def function_signup_button_pressed():
    st.session_state['current_page'] = 'Signup'
    st.session_state['signup_pressed'] = True