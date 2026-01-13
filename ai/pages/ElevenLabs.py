import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("ElevenLabs")
    st.markdown("""
    **ElevenLabs is an advanced AI-driven text-to-speech platform that enables users to create voice clonings and good for outbound calls, podcasts, audiobooks, and more.**
                """)
    
    st.markdown("ElevenLabs: https://elevenlabs.io/")

def main():
    SidebarNav()
    intro()


if __name__ == "__main__":
    main()


# https://www.monetizedmarketingtraining.com/ai-marketing-summit-2025-recordings-may150211705512687/ai-marketing-summit-2025-recordings-may/ai-image-summit-recording3ef61a987a3d/