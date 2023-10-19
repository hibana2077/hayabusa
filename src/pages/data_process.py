'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-10-18 00:46:42
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-10-19 15:21:41
FilePath: \hayabusa\src\pages\data_process.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utl import get_dataset_name_list
from pycaret.regression import *
from pycaret.classification import *
from pycaret.clustering import *
from pycaret.time_series import *

st.title("Data Process")

tab_pycaret , tab_manual = st.tabs(["Pycaret", "Manual"])

with tab_pycaret:
    st.write("## Pycaret Data Process")

    st.write("### Data Load")
    dataset_name = st.selectbox("Select Dataset", get_dataset_name_list(), index=None)

    st.write("### Basic Setting")

    st.write("### Scale And Transform")

    st.write("### Feature Engineering")

    st.write("### Feature Selection")

with tab_manual:
    st.write("## Manual Data Process")