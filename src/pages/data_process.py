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
    dataset_name = st.selectbox("Select Dataset", get_dataset_name_list())

    st.write("### Scale And Transform")

    st.write("### Feature Engineering")

    st.write("### Feature Selection")

with tab_manual:
    st.write("## Manual Data Process")