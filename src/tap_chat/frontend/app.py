import streamlit as st
import httpx

st.title("FastAPI + Streamlit Chatbot 🤖")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = httpx.post("http://localhost:8000/chat", json={"user_message": user_input})
        bot_reply = response.json()["response"]
        st.text_area("Bot:", value=bot_reply, height=100)
