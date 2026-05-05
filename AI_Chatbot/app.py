import streamlit as st
from chatbot import chatbot
from voice import get_voice_input

st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("🤖 AI Chatbot (ChatGPT Style)")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Text input
user_input = st.chat_input("Type your message...")

# Voice input button
if st.button("🎤 Speak"):
    user_input = get_voice_input()

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    response = chatbot(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)