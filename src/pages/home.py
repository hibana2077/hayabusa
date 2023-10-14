import streamlit as st

def Home():
    st.title("Home")
    st.write("Welcome to the home page")

st.title("Home")
st.write("Welcome to the home page")
st.write(f"Name in the main app: {st.session_state.name}")