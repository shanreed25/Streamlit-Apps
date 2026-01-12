import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("Machine Learning(ML)")

    st.markdown(""" **Machine learning is teaching computers to learn from data, find patterns, and make decisions or predictions without being told every detail.**
                - as humans we learn from experience to recognize things or make choices
                -  ML uses algorithms that change based on new information allowing them to get better over time
                """)
    
    st.markdown("## How Machine Learning Works")

    st.markdown("""
                ### :rainbow[Step 1: **Data Collection**]
                - Gather lots of examples or information about what you want the computer to learn
                """)

    st.markdown("""
                ### :rainbow[Step 2: **Training**]
                - Feed this data into a machine learning algorithm. The algorithm looks for patterns in the data
                """)
    
    st.markdown("""
                ### :rainbow[Step 3: **Model Creation**]
                - The algorithm creates a model based on the patterns it found
                """)
    
    st.markdown("""
                ### :rainbow[Step 4: **Prediction**]
                - When given new data, the model uses what it learned to make predictions or decisions
                """)
    
    st.markdown("""
                ### :rainbow[Step 5: **Improvement**]
                - As more data is collected, the model can be updated to improve its accuracy
                """)



def main():
    SidebarNav()
    intro()

if __name__ == "__main__":
    main()