import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.write("Hello from trading!")

if __name__ == "__main__":
    main()
