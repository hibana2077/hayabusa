from sklearn import datasets
import pandas as pd
import streamlit as st
import yaml
import os

st.write("Data Upload")

ta1 , tab2 = st.tabs(["Upload Dataset", "Sklearn Dataset", "Pandas Dataset"])