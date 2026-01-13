import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("AI Tools")

    st.markdown("""""")
    
    st.markdown("ideogram: https://ideogram.ai/")
    st.header("hailuoai: https://hailuoAI.video/")
    st.markdown("")


def main():
    SidebarNav()
    intro()


if __name__ == "__main__":
    main()