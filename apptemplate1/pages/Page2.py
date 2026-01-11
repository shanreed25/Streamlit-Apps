import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.write("Page 2!")
    
if __name__ == "__main__":
    main()
