import streamlit as st

st.title("Hello AI")
name = st.text_input("Your name")
st.write("You entered:", name)