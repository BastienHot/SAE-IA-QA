import streamlit as st

from login import view_login
from signup import view_signup
from chatbot import view_chatbot
from Ressources.Session import initialize_session

def main():

    initialize_session()

    if st.session_state['current_page'] == 'Login':
        view_login()

    if st.session_state['current_page'] == 'Signup':
        view_signup()
    
    if st.session_state['current_page'] == 'Chatbot':
        view_chatbot()

if __name__ == "__main__":
    main()
