import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.title("Getting Started with ChatGPT!")

    st.markdown("""
    #### :rainbow[Sign Up for ChatGPT]
    - **https://chatgpt.com**
                
    #### :rainbow[Configure Settings]
    - :green[**Help Keep Your Account Secure**] : Settings > Security > Enable Multi-Factor Authentication
    - :green[**Disable Improve The Model For Everyone**] : Data controls > Turn Off "Improve the model for everyone"
        - this stops your data from being used to train and improve the ChatGPT models
    - :green[**Memory Personalization**] : Personalization > Memory > Turn On "Reference chat history"
        - this saves your chat history
        - then you can recall it in a different session
        - also used to train the model and customize responses
    - :green[**Custom Instructions**] : Settings > Custom Instructions
        - set your preferences for how ChatGPT responds and what it knows about you
                """)
if __name__ == "__main__":
    main()


# https://www.monetizedmarketingtraining.com/ai-marketing-summit-2025-recordings-may150211705512687/ai-marketing-summit-2025-recordings-may/ai-image-summit-recording3ef61a987a3d/

# https://drive.google.com/drive/folders/1LiAa44LaKA8S81ItLlQhEvlxHyYaOTeg