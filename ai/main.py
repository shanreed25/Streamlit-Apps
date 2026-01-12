import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.write("Hello from Template 1!")


if __name__ == "__main__":
    main()