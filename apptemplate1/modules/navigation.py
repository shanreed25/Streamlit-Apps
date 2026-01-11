import streamlit as st

# this function will create a sidebar navigation menu
# it will override the default Streamlit sidebar
# creates a custom sidebar navigation menu
def SidebarNav():
    with st.sidebar:
        st.page_link('main.py', label='Landing Page', icon='✨')
        st.page_link('pages/Page1.py', label='Page 1', icon='📍')
        st.page_link('pages/Page2.py', label='Page 2', icon='📍')