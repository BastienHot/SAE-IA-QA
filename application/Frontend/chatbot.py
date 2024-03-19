import streamlit as st
import requests
from Ressources.Config import URL

def view_chatbot():
    view_history()

    if st.session_state['chat_id'] is None:
        st.title("HealthCare ChatBot")
        st.write("Welcome to the HealthCare ChatBot. Enter your question to start a new chat.")
        view_file_upload()
        view_chat()
    else:
        st.title(st.session_state['chat_history'][str(st.session_state['chat_id'])]['chat_title'])
        view_file_upload()
        for message in st.session_state['selected_chat']:
            if message['chat_message_is_ia'] == 1:
                with st.chat_message("assistant"):
                    st.write(message['chat_message'])
            else:
                with st.chat_message("user"):
                    st.write(message['chat_message'])
        view_chat()



def view_history(): 
    function_initialize_history()

    col1, col2, col3 = st.sidebar.columns([3, 1, 1])
    col1.write(st.session_state['user_name'])
    col3.button('🔒', on_click=function_logout_user)

    col1, col2, col3 = st.sidebar.columns([3, 1, 1])
    col1.write('Home')
    col3.button('➕', on_click=function_new_chat)

    st.sidebar.title('')

    for option in st.session_state.chat_history.values():
        col1, col2, col3 = st.sidebar.columns([3, 1, 1])
        col1.write(option['chat_title'], key=f"chat_title_{option['chat_id']}")
        col2.button('👀', key=f"show_{option['chat_id']}", on_click=function_show_chat, args=(option['chat_id'],))
        col3.button('🗑️', key=f"del_{option['chat_id']}", on_click=function_delete_chat, args=(option['chat_id'],))


def view_chat():
    col1, col2 = st.columns([7, 1])

    with col1:
        st.text_input("Enter your question", key='user_question', on_change=function_send_message)
    with col2:
        st.write('')
        st.write('')
        st.button('🔎', on_click=function_send_message)

def view_file_upload():
    st.file_uploader('Upload')  
    st.write('') 


def function_initialize_history():
    response = requests.get(URL + "/chatHistory", json={
        'user_id': st.session_state['user_id'],
        'user_is_connected': st.session_state['user_is_connected'],
    })

    st.session_state.chat_history = response.json()

def function_send_message():
    response = requests.post(URL + "/predict", json={
        'user_id': st.session_state['user_id'],
        'chat_id': st.session_state['chat_id'],
        'user_is_connected': st.session_state['user_is_connected'],
        'user_question': st.session_state['user_question']
    })

    content = response.json()
    
    if st.session_state['chat_id'] == None:      
        st.session_state['chat_id'] = int(content['chat_id'])
        function_initialize_history()

    st.session_state['user_question'] = ''

    function_show_chat(int(content['chat_id']))
    


def function_new_chat():
    st.session_state['chat_id'] = None
    st.session_state['selected_chat'] = None


def function_show_chat(chat_id):
    st.session_state['chat_id'] = int(chat_id)

    response = requests.get(URL + "/chatMessage", json={
        'user_id': st.session_state['user_id'],
        'user_is_connected': st.session_state['user_is_connected'],
        'chat_id': chat_id
    })

    content = response.json()
    st.session_state['selected_chat'] = content


def function_delete_chat(chat_id):
    if st.session_state['chat_id'] == chat_id:
        st.session_state['chat_id'] = None

    requests.post(URL + "/deleteChat", json={
        'user_id': st.session_state['user_id'],
        'chat_id': chat_id,
        'user_is_connected': st.session_state['user_is_connected'],
    })

    del st.session_state.chat_history[str(chat_id)]
    function_new_chat()

def function_logout_user():
    st.session_state['user_id'] = None
    st.session_state['user_name'] = None
    st.session_state['user_is_connected'] = False
    st.session_state['chat_history'] = {}
    st.session_state['selected_chat'] = {}
    st.session_state['user_question'] = ''
    st.session_state['chat_id'] = None
    st.session_state['current_page'] = 'Login'
    st.session_state['login_pressed'] = False
    st.session_state['signup_pressed'] = False