import streamlit as st

def page1():
    st.title("page1")
    st.write("Welcome to the page1 page")

st.title("page1")
st.write("Welcome to the page1 page")
st.write(f"Name in the main app: {st.session_state.name}")