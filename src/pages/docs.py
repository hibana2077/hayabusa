'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-10-18 00:46:42
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-01-02 18:49:01
FilePath: \hayabusa\src\pages\home.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import streamlit as st

st.title("Docs")

st.subheader("TL;DR")

st.markdown(
    """
    - Go to the **Data** page to upload and modify your data.
    - Go to the **Model** page to design and train your model.
    - Go to the **Evaluate** page to evaluate and download your model.
    """
)