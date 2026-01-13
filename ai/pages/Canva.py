import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("Canva AI")

    st.markdown(""" Canva AI is an integrated artificial intelligence feature within the Canva design platform that leverages AI technologies to enhance the user experience.
                It offers tools such as AI-powered design suggestions, image generation, background removal, and text enhancements to help users create visually appealing content more efficiently.
                """)
    
    st.markdown("Canva AI: https://www.canva.com/features/ai/")


def main():
    SidebarNav()
    intro()


if __name__ == "__main__":
    main()