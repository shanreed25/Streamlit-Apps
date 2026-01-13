import streamlit as st

# this function will create a sidebar navigation menu
# it will override the default Streamlit sidebar
# creates a custom sidebar navigation menu
def SidebarNav():
    with st.sidebar:
        st.page_link('main.py', label='Landing Page', icon='✨')
        st.page_link('pages/ChatGPT.py', label='ChatGPT', icon='📍')
        st.page_link('pages/Prompting.py', label='Prompting', icon='📍')
        st.page_link('pages/CustomVoice.py', label='Customize Your Voice', icon='📍')
        st.page_link('pages/ContentDetector.py', label='Content Detector', icon='📍')
        st.page_link('pages/MachineLearning.py', label='Machine Learning', icon='📍')
        st.page_link('pages/Hedra.py', label='Hedra AI', icon='📍')
        st.page_link('pages/Gemini.py', label='Google Gemini', icon='📍')
        st.page_link('pages/Canva.py', label='Canva AI', icon='📍')
        st.page_link('pages/SmithAI.py', label='Smith AI', icon='📍')
        st.page_link('pages/ElevenLabs.py', label='ElevenLabs', icon='📍')
        st.page_link('pages/HeyGen.py', label='HeyGen AI', icon='📍')