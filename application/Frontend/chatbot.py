import streamlit as st

def show_chatbot():
    if 'options' not in st.session_state:
        st.session_state.options = [{'name': 'LinkedIn Profil Consultation', 'content': 'Contenu de l\'Option 1'}, 
                                    {'name': 'Charger modèle GPT-2.', 'content': 'Contenu de l\'Option 2'}, 
                                    {'name': 'Flask arborescence MVC', 'content': 'Contenu de l\'Option 3'}]
        
    if 'selected_content' not in st.session_state:
        st.session_state['selected_content'] = None

    if 'home_selected' not in st.session_state:
        st.session_state['home_selected'] = True

    user_name = st.session_state.get('user_name', '')
    user_id = st.session_state.get('user_id', '')

    history()

    if st.session_state['home_selected']:
        st.write("Bienvenue sur la page d'accueil ! Sélectionnez une option pour afficher son contenu ou supprimer.")
        chat()
    elif st.session_state['selected_content']:
        st.write(st.session_state['selected_content'])


def history(): 
    col1, col2, col3 = st.sidebar.columns([3, 1, 1])
    col1.write('Home')
    col3.button('➕', on_click=show_home)

    for index, option in enumerate(st.session_state.options):
        col1, col2, col3 = st.sidebar.columns([3, 1, 1])
        col1.write(option['name'], key=f"name_{index}")
        col2.button('👀', key=f"show_{index}", on_click=show_content, args=(index,))
        col3.button('🗑️', key=f"del_{index}", on_click=delete_option, args=(index,))


def show_home():
    st.session_state['home_selected'] = True
    st.session_state['selected_content'] = None


def show_content(index):
    st.session_state['selected_content'] = st.session_state.options[index]['content']
    st.session_state['home_selected'] = False


def delete_option(index):
    del st.session_state.options[index]
    st.session_state['home_selected'] = False 
    show_home()

def chat():
    st.text_area('Chatbot', key='chatbot', height=100, max_chars=200, on_change=send_message)
    st.button('Envoyer', on_click=send_message)

def send_message():
    st.session_state.options.append({'name': 'Nouvelle option', 'content': 'Contenu de la nouvelle option'})
    st.session_state['home_selected'] = True
    st.session_state['selected_content'] = None