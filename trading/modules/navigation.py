import streamlit as st

def SidebarNav():
    with st.sidebar:
        st.page_link('main.py', label='Introduction', icon='✨')
        st.page_link('pages/DayTrading.py', label='Day Trading', icon='📍')
        st.page_link('pages/SwingTrading.py', label='Swing Trading', icon='📍')