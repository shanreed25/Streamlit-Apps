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
                - You should also label the data to help the computer understand it better
                - For example, if you're teaching it to recognize pictures of cats, you'd collect many images of cats and label them as "cat"
                    - You should also include examples that are not cats to help the model learn the difference
                    - The data should be diverse and cover different scenarios so the model can learn well
                    - The model creates kind of a map of the data or cheetsheet with labels that like "cat", "not cat", "dog", "car", etc.
                - The more diverse and comprehensive the data, the better the model can learn
                """)

    st.markdown("""
                ### :rainbow[Step 2: **Training**]
                - Feed this data into a machine learning algorithm. The algorithm looks for patterns in the data
                - For example, it might notice that cats often have pointy ears, whiskers, and certain shapes
                - The algorithm adjusts itself to better recognize these patterns over many iterations
                - This process is called training because the algorithm is learning from the data
                - Testing is also done during training to see how well the model is learning and to make adjustments as needed
                """)
    
    st.markdown("""
                ### :rainbow[Step 3: **Model Creation**]
                - The algorithm creates a model based on the patterns it found
                - This model is like a set of rules or a cheat sheet that the computer can use to make decisions
                - For example, the model might say "if it has pointy ears and whiskers, it's probably a cat"
                """)
    
    st.markdown("""
                ### :rainbow[Step 4: **Prediction**]
                - When given new data, the model uses what it learned to make predictions or decisions
                - For example, if you show it a new picture, it will analyze the features and decide if it's a cat or not based on its training
                - The model might say "this picture has pointy ears and whiskers, so it's a cat"
                """)
    
    st.markdown("""
                ### :rainbow[Step 5: **Improvement**]
                - As more data is collected, the model can be updated to improve its accuracy
                - This is called retraining, where the model learns from new examples to get better over time
                - For example, if the model makes a mistake, you can show it the correct answer and it will adjust its rules accordingly
                - This continuous learning helps the model adapt to new situations and improve its performance
                """)



def main():
    SidebarNav()
    intro()

if __name__ == "__main__":
    main()

# https://drive.google.com/drive/folders/1LiAa44LaKA8S81ItLlQhEvlxHyYaOTeg