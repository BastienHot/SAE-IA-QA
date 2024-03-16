import streamlit as st

from login import show_login
from signup import show_signup
from chatbot import show_chatbot

def main():

    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'Login'

    if 'login_pressed' not in st.session_state:
        st.session_state['login_pressed'] = False

    if 'signup_pressed' not in st.session_state:
        st.session_state['signup_pressed'] = False

    if st.session_state['current_page'] == 'Login':
        show_login()

    if st.session_state['current_page'] == 'Signup':
        show_signup()
    
    if st.session_state['current_page'] == 'Chatbot':
        show_chatbot()

if __name__ == "__main__":
    main()
