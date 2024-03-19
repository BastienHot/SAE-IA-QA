import streamlit as st

def initialize_session():
    # APP
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'Login'

        
    # LOGIN
    if 'login_pressed' in st.session_state:
        st.session_state['login_pressed'] = False 

    if 'user_id' not in st.session_state:
        st.session_state['user_id'] = None

    if 'user_name' not in st.session_state:
        st.session_state['user_id'] = None
        
    if 'user_is_connected' not in st.session_state:
        st.session_state['user_is_connected'] = False


    # SIGNUP
    if 'signup_pressed' in st.session_state:
        st.session_state['signup_pressed'] = False 


    # CHAT
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = {}
    
    if 'selected_chat' not in st.session_state:
        st.session_state['selected_chat'] = {}

    if 'user_question' not in st.session_state:
        st.session_state['user_question'] = ''

    if 'chat_id' not in st.session_state:
        st.session_state['chat_id'] = None
    
    