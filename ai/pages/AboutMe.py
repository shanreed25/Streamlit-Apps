import streamlit as st
from modules.navigation import SidebarNav




def main():
    SidebarNav()
    st.title("Shannon Reed")

    st.write("I am Shannon Reed, my intrest in AI comes from my background in technology. I have spent many years learning "
    "and working with technology and AI has rapidly become a passion of mine. Learning to work with AI has been a challenging but exciting journey. ")

if __name__ == "__main__":
    main()