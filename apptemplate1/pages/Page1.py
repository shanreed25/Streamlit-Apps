import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.write("Page 1!")

if __name__ == "__main__":
    main()
