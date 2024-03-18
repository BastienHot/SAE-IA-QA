import streamlit as st
import requests
from Ressources.Config import URL

def view_chatbot():
    view_history()

    if st.session_state['chat_id'] is None:
        st.write("Bienvenue sur la page d'accueil ! Sélectionnez une option pour afficher son contenu ou supprimer.")
        view_chat()
    else:
        st.write("selection")
        view_chat()


def view_history(): 
    function_initialize_history()

    col1, col2, col3 = st.sidebar.columns([3, 1, 1])
    col1.write('Home')
    col3.button('➕', on_click=function_new_chat)

    for option in st.session_state.options.values():
        col1, col2, col3 = st.sidebar.columns([3, 1, 1])
        col1.write(option['chat_title'], key=f"chat_title_{option['chat_id']}")
        col2.button('👀', key=f"show_{option['chat_id']}", on_click=function_show_chat, args=(option['chat_id'],))
        col3.button('🗑️', key=f"del_{option['chat_id']}", on_click=function_delete_chat, args=(option['chat_id'],))

def view_chat():
    st.text_area('Chatbot', key='user_question', height=100)
    st.button('Envoyer', on_click=function_send_message)




def function_initialize_history():
    response = requests.get(URL + "/chatHistory", json={
        'user_id': st.session_state['user_id'],
        'user_is_connected': st.session_state['user_is_connected'],
    })

    content = response.json()
    print(content, "content")
    if 'options' not in st.session_state:
        st.session_state.options = content
        

def function_send_message():
    response = requests.post(URL + "/predict", json={
        'user_id': st.session_state['user_id'],
        'chat_id': st.session_state['chat_id'],
        'user_is_connected': st.session_state['user_is_connected'],
        'user_question': st.session_state['user_question']
    })

    content = response.json()[0]

    st.session_state.options.update({ 
        content['chat_id'] : {
            'chat_id':int(content['chat_id']),
            'chat_title':content['chat_title'], 
        }
    })

    st.session_state['user_question'] = ''
    st.session_state['chat_id'] = int(content['chat_id'])

    function_initialize_history()


def function_new_chat():
    st.session_state['chat_id'] = None
    st.session_state['selected_content'] = None


def function_show_chat(chat_id):
    st.session_state['chat_id'] = int(chat_id)

    print(st.session_state.options[str(chat_id)])



def function_delete_chat(chat_id):
    if st.session_state['chat_id'] == chat_id:
        st.session_state['chat_id'] = None

    response = requests.post(URL + "/deleteChat", json={
        'user_id': st.session_state['user_id'],
        'chat_id': chat_id,
        'user_is_connected': st.session_state['user_is_connected'],
    })

    del st.session_state.options[str(chat_id)]
    function_new_chat()