import streamlit as st
import httpx

FASTAPI_URL = "https://tap-chat-backend-cfcaaxdkcqcsapf4.westeurope-01.azurewebsites.net/"

st.title("FastAPI + Streamlit Chatbot 🤖")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = httpx.post(f"{FASTAPI_URL}/chat", json={"user_message": user_input})
        bot_reply = response.json()["response"]
        st.text_area("Bot:", value=bot_reply, height=100)
