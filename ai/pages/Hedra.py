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
                #### :green[Example Prompt To Generate An Image ]
                :blue[**"Create a African American women between the ages of 35 to 40 with medium length locs pulled up in a high ponytail, 
                wearing purple glasses and a purple jumpsuit she should be pixar style"**]

                #### :violet[**You can use ChatGPT to help you come up with better prompts for generating images!**]

                ##### :green[Example Prompt To Refine Your Prompt]
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
                
                #### :violet[**You can use ChatGPT to help you come up with better prompts for generating videos!**]
                #### :green[Example ChatGPT Prompt To Generate A Video Script]
                :blue[**"ok- now i would like for the women to tell me what her goal is for learning AI to create social 
                media content and for her professional career as a software developer. She has ideas of the things she 
                can create with AI but doesn't really know how to implement them in a way to generate income."**]

                #### :green[Example ChatGPT Prompt To Refine to describe the actions of the character in the video ]
                :blue[**"Rewrite this prompt for a AI video generator to make it better: The women looks forward and then starts 
                         speaking, while smiling and making gestures with her hands and moving her head in a way a human would do when speaking."**]
                
                #### :green[ChatGPT Rewritten Prompt ]
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


# https://www.monetizedmarketingtraining.com/ai-marketing-summit-2025-recordings-may150211705512687/ai-marketing-summit-2025-recordings-may/ai-image-summit-recording3ef61a987a3d/


# https://indecisive-enquiry-647.notion.site/Hedra-Training-2000cfd9f3e08009984af31ea9d06bb3