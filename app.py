import streamlit as st
from SmartCheck import smartcheck_interface
from SmartRound import smartround_interface

st.set_page_config(page_title="SmartRound", layout="centered")

st.sidebar.title("SmartRound")
page = st.sidebar.radio("Escolha uma função:", ["SmartCheck", "SmartRound Enfermaria"])

if page == "SmartCheck":
    smartcheck_interface()
elif page == "SmartRound Enfermaria":
    smartround_interface()
