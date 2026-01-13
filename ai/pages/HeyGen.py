import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("HeyGen AI")

    st.markdown(""" HeyGen AI is an integrated artificial intelligence feature within the HeyGen platform that leverages AI technologies to enhance the user experience.
                It offers tools such as AI-powered design suggestions, image generation, background removal, and text enhancements to help users create visually appealing content more efficiently.
                """)
    
    st.markdown("HeyGen AI: https://www.heygen.com/ai")


def main():
    SidebarNav()
    intro()


if __name__ == "__main__":
    main()

    # https://www.monetizedmarketingtraining.com/ai-marketing-summit-2025-recordings-june/ai-marketing-summit-2025-recordings-june/ai-image-summit-recording3ef61a987a3d/