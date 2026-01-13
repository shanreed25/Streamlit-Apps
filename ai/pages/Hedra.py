import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("Hedra AI")
    st.markdown("""
                **HEDRA AI is an AI platform that offers AI-powered tools and services such 
                as text generation, image generation, and more> It aims to make AI accessible 
                to everyone and is user-friendly, allowing you to easily create 
                and utilize AI models without needing extensive technical knowledge**
                """)

def hedraImage():
    st.markdown("### :rainbow[Creating an Image with Hedra]")
    st.markdown("""
                #### :green[Example Prompt ]
                :blue[**"Create a African American women between the ages of 35 to 40 with medium length locs pulled up in a high ponytail, 
                wearing purple glasses and a purple jumpsuit she should be pixar style"**]

                #### :green[Example Prompt: Add this prompt to ChatGPT to refine it further ]
                :blue[**"Rewrite this prompt for a AI image generator to make it better: A African American women between the ages of 35 to 40 with medium length locs 
                            pulled up in a high ponytail, with a slim face and wearing purple glasses and a purple fitted jumpsuit she should be pixar style**"]
                
                #### :green[ChatGPT Rewritten Prompt ]
                :blue[**"A Pixar-style animated character of an African American woman aged 35-40. She has a slim, elegant face and medium-length locs styled into a high 
                         ponytail. She is wearing stylish purple glasses and a fitted purple jumpsuit. The character has expressive eyes, warm brown skin tones, soft 
                         lighting, smooth textures, and the polished, colorful look typical of Pixar animation."**]


                :red[Use the refined prompt in Hedra to generate a better image]
                """)

def hedraVideo():
    st.markdown("### :rainbow[Creating a Video with Hedra]")
    st.markdown("""
                #### :green[Example Prompt ]
                :blue[**"The woman faces the camera and begins speaking after a brief natural pause, wearing a warm, confident smile. 
                As she talks, she uses relaxed, expressive hand gestures to emphasize key points without overexaggeration. Her head 
                and upper body move naturally—small nods, gentle tilts, and slight shifts that reflect engagement and thoughtfulness. 
                Her facial expressions are lively yet controlled, with expressive eyes that stay facing forward and natural mouth movements, creating a 
                conversational, authentic, human-like delivery that feels approachable and professional."**]

                """)

def hedraVideo1():
        st.markdown("""
                ### :rainbow[Step 1: **Sign Up for a Free Account at Hedra.com**]
                """)
        
def hedraVideo2():
        st.markdown("""
                ### :rainbow[Step 2: **Start Creating**]
                """)
        


#         My goal for learning AI is to turn my ideas into things people actually want to use, share, and pay for. I want to create content that blends creativity with technical insight.

# Professionally I want to use it to prototype ideas faster, build small products and tools on my own, automate parts of development and content creation

# I have a lot of ideas but my challenge is turning those ideas into real income streams. I want to learn how to validate ideas quickly and build things people actually want.

def main():
    SidebarNav()
    intro()
    st.divider()

    hedraImage()
    st.divider()

    hedraVideo()
    st.divider()



if __name__ == "__main__":
    main()