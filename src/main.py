'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-10-14 12:20:25
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-10-14 12:47:40
FilePath: \haya\src\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import streamlit as st
from session_init import init

if __name__ == '__main__':
        
    init()

    st.title("Hayabusa")
    st.write("Welcome to this multi-page app built with Streamlit")
    if st.session_state.name == "":
        name = st.text_input("Name")
        st.session_state.name = name
    if st.session_state.user_name == "":
        user_name = st.text_input("User Name")
        st.session_state.user_name = user_name
    if st.session_state.user_password == "":
        user_password = st.text_input("User Password")
        st.session_state.user_password = user_password
    if st.session_state.user_email == "":
        user_email = st.text_input("User Email")
        st.session_state.user_email = user_email
    if st.session_state.discord_webhook == "":
        discord_webhook = st.text_input("Discord Webhook")
        st.session_state.discord_webhook = discord_webhook