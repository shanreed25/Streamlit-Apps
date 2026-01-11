import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.write("Day Trading!")

if __name__ == "__main__":
    main()
