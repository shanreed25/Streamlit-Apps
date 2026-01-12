import streamlit as st
from modules.navigation import SidebarNav

def intro():
    st.title("Customize Your Voice")
    st.markdown("""
    **Your voice is your superpower and these tools should serve your voice, not replace it.
      Your voice isn't just how you write, it's how you connect, how you lead, how you change things.
      This is a step-by-step guide to teaching AI tools to write in your authentic voice.**
                """)

def step1():
    st.markdown("""
    ## :rainbow[Step 1: Gather Your Materials]
    :green[**Collect the content that reflects your authentic voice. This could include:**]
    - Your bio or personal statement
    - Samples of your writing or speaking style
        - Transcripts of your talks, webinars, or interviews
        - Articles, blog posts, or essays you've written
        - Emails or newsletters you've sent
        - Social media posts or comments that showcase your style
        - Any other written content that captures your tone and mannerisms
                """)
    
def step2():
        st.markdown("""
    ## :rainbow[Step 2: Feed Your Voice to AI]
    #### :green[Example Prompt 1]
    :blue[**"I would like for you to write for me as my ghostwriter. I will be giving you my bio and two 
            [transcripts of trainings / articles i have written] so that you can learn
            about me and learn my writing and teaching style and tone so that you can 
            write for me as me. Do you understand?"**]
    
    :red[**Then provide the AI with your bio and 2-3 samples of your actual work**]
                
    #### :green[Example Prompt 2]
    :blue[**"I want you to be my ghostwriter. I'm sharing my bio and [2-3] samples 
        of my actual work such as transcripts, articles, or content I've created. 
        Study these carefully. Learn my voice, my rhythm, my way of connecting
        with people. Pay attention to how I structure thoughts, what words I 
        choose, and how I make people feel. Do you understand?"**]
                
    :red[**Then share your materials.**]
                """)
    

def step3():
    st.markdown("""
    ## :rainbow[Step 3: Get Your Voice Analysis]
    #### :green[Example Prompt 1]
    :blue[**"Based on what you've read, how would you describe my writing style and voice? 
             If someone wanted to write exactly like me, what would they need to know? Include
             my tone and energy, phrases I use often, how I typically start conversations or 
             content, how I close or sign off, the emotional journey I take readers on, any 
             unique patterns in how I structure ideas, what makes my voice distinctly mine**]
                
    :red[**Save this analysis, you'll need it for the next step.**]
                
    #### :green[Example Prompt 2]
    :blue[**"How would you describe my writing style and tone? How would you describe my content
             style to someone who wanted to write exactly like me? What phrases do I use often? 
             How do I usually start and end my content? Etc**]
                
    :red[**Save this analysis, you'll need it for the next step.**]
                    """)

def step4():
    st.markdown("""
    ## :rainbow[Step 4: Create Your Voice Blueprint]
    #### :green[Example Prompt ]
    :blue[**"Rewrite this in first person as if I am describing this to my ghostwriter."**]
                
    :red[**This becomes your custom voice guide.**]
                
    #### :green[Example Prompt 2]
    :blue[**"Take that analysis and rewrite it in first person, as if I'm giving instructions to my
             ghostwriter. Make it sound like me talking about my own voice. Start with 'I write 
             from...' or 'My voice is...' Keep my authentic tone throughout."**]
                
    :red[**This becomes your custom voice guide.**]
                    """)

def step5():
    st.markdown("""
    ## :rainbow[Step 5: Implement Your Voice Guide]
    ### For ChatGPT Users
    1. Go to **Settings > Personalization > Custom Instructions**
    2. In the **top box**: Paste your first-person voice guide
    3. In the **bottom box**: Paste your bio
    4. Toggle **Enable for new chats** to ON
    5. Save
                
    ### For Claude Users
    1. Click your profile icon > **Settings** > **Profile**
    2. Add your bio and voice guide
    3. Save
    
    ### For Other AI Tools
    1. Save your voice guide as a file (title it "My Voice Guide - [Your Name]")
    2. At the start of each session, share: *"Here's my voice guide. Please write in this style."*
    3. Paste your guide before making any content requests
                
    #### :green[Example Prompt ]
    :blue[**"Using my voice guide, write a [blog post/email/social media update] about [topic]. 
             Make sure it sounds like me and follows the style and tone I've established."**]
                
    :red[**Review and refine the output as needed.**]
                    """)
    

def voiceGuideTemplate():
    st.markdown("""
    ## :rainbow[Voice Guide Template]
    :green[**After completing the process, your voice guide might look like this:**]
                
    #### :green[Template 1]
    :blue[**"I write from a place of [authenticity/empathy/humor/etc.]
    My tone is usually [casual/formal/enthusiastic/etc.].
    I often use phrases like [insert common phrases].
    I start my content by [describe typical openings].
    I end my content by [describe typical closings].
    My writing structure typically includes [describe structure patterns].
    The emotional journey I take my audience on is usually [describe emotional tone]."**]
                
    #### :green[Template 2]
    :blue[**"I write from [core place - heart/experience/wisdom]. My tone is [qualities]. I believe in [core beliefs about communication].
    When I write, I [describe your approach]. I often say things like ["example phrases"] because [why these matter to you].
    I start pieces with [your opening style]. I close with [your closing style]. I want readers to feel [desired impact].
    My voice is [final description of what makes you unique]"**.]

                """)    
def bestPractices():
    st.markdown("""
    ## :rainbow[Best Practices for Using Your Custom Voice Guide]
    - **Consistency is Key**: Always use your voice guide at the start of new sessions to maintain consistency.
    - **Be specific**: The more detail in your voice guide, the better the output.
    - **Refine Over Time**: As you use AI tools more, update your voice guide every few months with new insights or changes in your style.
    - **Test & Provide Feedback**: If the AI's output doesn't match your voice, provide specific feedback to help it improve. Ask AI to write a short piece. Does it sound like you? Adjust as needed.
    - **Combine with Other Settings**: Use other personalization settings in the AI tool to further tailor responses.
    - **Stay Authentic**: Regularly review outputs to ensure they align with your authentic voice and make adjustments as needed. Don't sanitize your voice. Your authenticity is your superpower.
                """)

def main():
    SidebarNav()
    intro()
    st.divider()

    step1()
    st.divider()

    step2()
    st.divider()

    step3()
    st.divider()

    step4()
    st.divider()

    step5()
    st.divider()

    voiceGuideTemplate()
    st.divider()

    bestPractices()
    st.divider()
    
    



if __name__ == "__main__":
    main()
