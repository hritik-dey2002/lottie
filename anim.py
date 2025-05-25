import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/

# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

# lottie_coding = load_lottiefile("anim.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/b39b11fd-87c3-441d-8431-21cddebe4c21/rpmLvaQA4l.json")
st_lottie(
            lottie_hello,
            # speed=1,
            # reverse=False,
            # loop=True,
            # quality="low", # medium ; high
            # renderer="svg", # canvas
            # height=None,
            # width=None,
            key=None,
        )

# with st.container():
#     row1, row2 = st.columns((1,2))
#     with row1:
        
#         st_lottie(
#             lottie_hello,
#             # speed=1,
#             # reverse=False,
#             # loop=True,
#             # quality="low", # medium ; high
#             # renderer="svg", # canvas
#             # height=None,
#             # width=None,
#             key=None,
#         )
#     with row2:

#         st_lottie(
#             lottie_coding,
#             # speed=1,
#             # reverse=False,
#             # loop=True,
#             # quality="low", # medium ; high
#             # renderer="svg", # canvas
#             # height=None,
#             # width=None,
#             key=None,
#         )
# with st.container():
#     row1, row2, row3= st.columns(3)
#     with row1:
#         st_lottie(
#             lottie_hello,
#             # speed=1,
#             # reverse=False,
#             # loop=True,
#             # quality="low", # medium ; high
#             # renderer="svg", # canvas
#             # height=None,
#             # width=None,
#             key=None,
#         )
#     with row3:

#         st_lottie(
#             lottie_coding,
#             # speed=1,
#             # reverse=False,
#             # loop=True,
#             # quality="low", # medium ; high
#             # renderer="svg", # canvas
#             # height= 500,
#             # width= 500,
#             key=None,
#         )


page_bg_img = f"""
                                <style>
                                [data-testid="stAppViewContainer"] > .main {{
                                background-image: url("https://i.postimg.cc/hGgH6t2C/Untitled-design-1.png");

                                background-position: center center;

                                /* Make image fixed */
                                background-attachment: fixed;

                                /* Not repeat images */
                                background-repeat: no-repeat;

                                /* Set background size auto */
                                background-size: 100%;
                                }}



                                [data-testid="stHeader"] {{
                                background: rgba(0,0,0,0);
                                }}

                                </style>
                                """

st.markdown(page_bg_img, unsafe_allow_html=True)


# import json
# import requests  # pip install requests
# import streamlit as st  # pip install streamlit
# from streamlit_lottie import st_lottie  # pip install streamlit-lottie

# # Function to load Lottie animation from a URL
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # Load the Lottie animation
# lottie_hello = load_lottieurl("https://lottie.host/581ab6d3-c1ab-4a63-bf18-77f826e913ae/c2Yl9CcaxG.json")

# # Add custom CSS for corner positioning
# st.markdown(
#     """
#     <style>
#     .corner-lottie {
#         position: fixed;
#         top: 20px;
#         buttom: 20px;
#         z-index: 1000;
#         width: 150px;
#         height: 150px;
#     }
#     </style>
#     <div class="corner-lottie">
#         <div id="lottie-animation"></div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # Embed Lottie animation
# if lottie_hello:
#     st_lottie(lottie_hello, height=150, width=150, key="corner_animation")

# # Main Content of the App
# st.title("Streamlit App with Corner Animation")
# st.write(
#     """
#     This is an example of how to display a Lottie animation in the corner of the Streamlit app.
#     The rest of your app content goes here.
#     """
# )

# import requests
# import streamlit as st
# from streamlit_lottie import st_lottie
# from PIL import Image


# # Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
# st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()


# # Use local CSS
# # def local_css(file_name):
# #     with open(file_name) as f:
# #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# # local_css("style/style.css")

# # ---- LOAD ASSETS ----
# lottie_coding = load_lottieurl("https://lottie.host/581ab6d3-c1ab-4a63-bf18-77f826e913ae/c2Yl9CcaxG.json")
# # img_contact_form = Image.open("images/yt_contact_form.png")
# # img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# # ---- HEADER SECTION ----
# with st.container():
#     st.subheader("Hi, I am Sven :wave:")
#     st.title("A Data Analyst From Germany")
#     st.write(
#         "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
#     )
#     st.write("[Learn More >](https://pythonandvba.com)")

# # ---- WHAT I DO ----
# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("What I do")
#         st.write("##")
#         st.write(
#             """
#             On my YouTube channel I am creating tutorials for people who:
#             - are looking for a way to leverage the power of Python in their day-to-day work.
#             - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
#             - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
#             - are working with Excel and found themselves thinking - "there has to be a better way."

#             If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
#             """
#         )
#         st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
#     with right_column:
#         st_lottie(lottie_coding, height=300, key="coding")

# # ---- PROJECTS ----
# # with st.container():
# #     st.write("---")
# #     st.header("My Projects")
# #     st.write("##")
# #     image_column, text_column = st.columns((1, 2))
# #     with image_column:
# #         st.image(img_lottie_animation)
# #     with text_column:
# #         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
# #         st.write(
# #             """
# #             Learn how to use Lottie Files in Streamlit!
# #             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
# #             In this tutorial, I'll show you exactly how to do it
# #             """
# #         )
# #         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# # with st.container():
# #     image_column, text_column = st.columns((1, 2))
# #     with image_column:
# #         st.image(img_contact_form)
# #     with text_column:
# #         st.subheader("How To Add A Contact Form To Your Streamlit App")
# #         st.write(
# #             """
# #             Want to add a contact form to your Streamlit website?
# #             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
# #             """
# #         )
# #         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# # # ---- CONTACT ----
# # with st.container():
# #     st.write("---")
# #     st.header("Get In Touch With Me!")
# #     st.write("##")

# #     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
# #     contact_form = """
# #     <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
# #         <input type="hidden" name="_captcha" value="false">
# #         <input type="text" name="name" placeholder="Your name" required>
# #         <input type="email" name="email" placeholder="Your email" required>
# #         <textarea name="message" placeholder="Your message here" required></textarea>
# #         <button type="submit">Send</button>
# #     </form>
# #     """
# #     left_column, right_column = st.columns(2)
# #     with left_column:
# #         st.markdown(contact_form, unsafe_allow_html=True)
# #     with right_column:
# #         st.empty()

