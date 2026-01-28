import streamlit as st
import pandas as pd



data = pd.read_csv(r"C:\Users\hp\Desktop\Vkaps_task\6.Streamlit\student_details.csv")

st.write(data.describe())