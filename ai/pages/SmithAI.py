import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("Smith AI")
    st.markdown("""
    **Smith AI is a virtual receptionist and client engagement platform that utilizes artificial intelligence to provide businesses with 24/7 customer support and lead management**
                """)
    
    st.markdown("Smith AI: https://smith.ai/")
    st.write("First Month Free with code: INNOVISION")



    # https://www.monetizedmarketingtraining.com/ai-marketing-summit-2025-recordings-may150211705512687/ai-marketing-summit-2025-recordings-may/ai-image-summit-recording3ef61a987a3d/


def main():
    SidebarNav()
    intro()

if __name__ == "__main__":
    main()