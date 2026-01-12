import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.title("Prompting")
    st.markdown("""
    #### :rainbow[A Prompt are the instructions you give to an AI model to generate a desired output.]
                """)
    
    st.markdown("""
    #### :rainbow[TADAA Prompting Framework]
    **A step-by-step guide to teaching AI tools to write in your authentic voice. Because your voice is your power, and these tools should amplify it, not erase it.**
    - :orange[**T**]:green[rain] : Before creating a prompt, train the AI on relevant information or context
    - :orange[**A**]:green[sk] : Clearly state the task or question you want the AI to address.
    - :orange[**D**]:green[igging Deeper] : Provide additional details, constraints, or examples to refine the AI's understanding.
    - :orange[**A**]:green[dditional Content] : Include any supplementary information that may help the AI generate a more accurate response.
    - :orange[**A**]:green[ssemble] : Combine all the elements into a coherent prompt for the AI to process.
                """)
    
    st.markdown("""
    ## :rainbow[Step 1: Gather Your Materials]
                """)
    st.markdown("""
    ## :rainbow[Step 2: TRAIN]
    **Feed Your Voice to AI**
    #### :green[Example Prompt 1]
    :blue[**"I would like for you to write for me as my ghostwriter. I will be giving you my bio and two 
            [transcripts of trainings / articles i have written] so that you can learn
            about me and learn my writing and teaching style and tone so that you can 
            write for me as me. Do you understand?"**]
    
    :red[**Then provide the AI with your bio and 2-3 samples of your actual work**]
                
    #### :green[Example Prompt 2]
    :blue[**"I want you to be my ghostwriter. I'm sharing my bio and [2-3] samples 
        of my actual work — transcripts, articles, or content I've created. 
        Study these carefully. Learn my voice, my rhythm, my way of connecting
        with people. Pay attention to how I structure thoughts, what words I 
        choose, and how I make people feel. Do you understand?"**]
                
    :red[**Then share your materials.**]
                """)
    


    st.markdown("""
    ## :rainbow[Step 3: ASK]
                    """)
    

    st.markdown("""
    ## :rainbow[Step 4: DIGGING DEEPER]
                    """)
    

    st.markdown("""
    ## :rainbow[Step 5: ADDITIONAL CONTENT]
                    """)
    

    st.markdown("""
    ## :rainbow[Step 6: ASSEMBLE]
                    """)



if __name__ == "__main__":
    main()
