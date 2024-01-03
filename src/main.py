'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-01-02 21:43:38
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-01-03 18:23:40
FilePath: \hayabusa\src\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from operator import index
import streamlit as st
import plotly.express as px
from ydata_profiling import ProfileReport
import pandas as pd
import pickle
import time
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset/') == False:
    os.mkdir('./dataset/')
if os.path.exists('./model/') == False:
    os.mkdir('./model/')
if os.path.exists('./pipeline/') == False:
    os.mkdir('./pipeline/')

with st.sidebar:
    st.title("AutoML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.drop("Unnamed: 0", axis=1, inplace=True)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)
        st.session_state['df'] = df

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    df:pd.DataFrame = st.session_state['df']
    pr = ProfileReport(df, title="Profiling Report")
    st_profile_report(pr)

if choice == "Modelling": 
    df:pd.DataFrame = st.session_state['df']
    chosen_target = st.selectbox('Choose the Target Column', df.columns)
    ml_task = st.selectbox('Choose the ML Task', ['Classification', 'Regression'])
    if st.button('Run Modelling'):
        if ml_task == 'Classification':
            from pycaret.classification import setup, compare_models, pull, save_model, get_config
            setup(df, target=chosen_target)
            setup_df = pull()
            st.dataframe(setup_df)
            best_model = compare_models(exclude=['lightgbm'])
            compare_df = pull()
            st.dataframe(compare_df)
            save_model(best_model, 'best_model')
            save_model(best_model, f"./model/{chosen_target}_{time.time()}")
            pipeline = get_config('pipeline')
            st.write(pipeline)
            # save the pipeline
            with open('pipeline.pkl', 'wb') as f:
                pickle.dump(pipeline, f)
        else:
            from pycaret.regression import setup, compare_models, pull, save_model
            setup(df, target=chosen_target)
            setup_df = pull()
            st.dataframe(setup_df)
            best_model = compare_models(exclude=['lightgbm'])
            compare_df = pull()
            st.dataframe(compare_df)
            save_model(best_model, 'best_model')
            save_model(best_model, f"./model/{chosen_target}_{time.time()}")
            pipeline = get_config('pipeline')
            st.write(pipeline)
            # save the pipeline
            with open('pipeline.pkl', 'wb') as f:
                pickle.dump(pipeline, f)

if choice == "Download": 
    with open('best_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="best_model.pkl")
    with open('pipeline.pkl', 'rb') as f:
        st.download_button('Download Pipeline', f, file_name="pipeline.pkl")