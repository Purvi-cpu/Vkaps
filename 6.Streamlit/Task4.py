import openai
import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

st.title("Chat-App")
load_dotenv()
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.text_area("Enter your prompt")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role":"user","content":prompt})
    response = f"Assistant: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role":"assistant","content": response})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        stream = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1:novita",
            messages=st.session_state.messages,
            stream=True,
        )

        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                full_response += delta.content
                message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant","content": full_response})
