from utils.openai import OpenAI

import streamlit as st

openai = OpenAI()


def display_spinner():
    with st.spinner("Wait for it..."):
        query = st.session_state["input_text"]
        resp = openai.chat(query)
        st.session_state.query_resp = resp


TITLE = "Project Lugia"
DESCRIPTION = """
                Introducing ChatGPT Language Assistant -
                Your AI-powered Conversation Companion! 
                Engage in dynamic conversations on any topic, get human-like responses in real-time, and customize the language style. 
                Perfect for content creation, research, translation, and more. 
                Say hello to intelligent conversations with ChatGPT!
            """

st.title(TITLE)
st.markdown(DESCRIPTION)

st.text_area(
    "Your input text",
    """
    What is your name?  
    """,
    key="input_text",
)

st.button("send", on_click=display_spinner)
st.text_area("Response", st.session_state.get("query_resp", ""))
