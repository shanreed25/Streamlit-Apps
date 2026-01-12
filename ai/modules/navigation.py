import streamlit as st

# this function will create a sidebar navigation menu
# it will override the default Streamlit sidebar
# creates a custom sidebar navigation menu
def SidebarNav():
    with st.sidebar:
        st.page_link('main.py', label='Landing Page', icon='✨')
        st.page_link('pages/ChatGPT.py', label='ChatGPT', icon='📍')
        st.page_link('pages/Prompting.py', label='Prompting', icon='📍')