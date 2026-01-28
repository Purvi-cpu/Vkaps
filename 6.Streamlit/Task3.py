import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)
prompt = st.text_area("Enter your prompt")
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1:novita",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
)



if st.button("generat"):
    if prompt.strip():
        result = completion.choices[0].message
        st.write(result)
    else: 
        st.write("Write some prompt")