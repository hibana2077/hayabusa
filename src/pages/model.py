'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-10-14 14:25:29
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-10-14 16:34:04
FilePath: \haya\src\pages\model.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import xgboost
import catboost
import lightgbm
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, OPTICS
from data import problem_specific_model_description_dict, required_parameters_dict, problem_type_to_model_type_dict, hyperparameter_range_dict

model_dict = {
    "Classification": {
        "XGBoost": xgboost.XGBClassifier,
        "CatBoost": catboost.CatBoostClassifier,
        "LightGBM": lightgbm.LGBMClassifier,
        "RandomForest": RandomForestClassifier,
        "Logistic Regression": LogisticRegression,
        "SVC": SVC,
        "KNeighborsClassifier": KNeighborsClassifier,
        "GaussianNB": GaussianNB,
    },
    "Regression": {
        "XGBoost": xgboost.XGBRegressor,
        "CatBoost": catboost.CatBoostRegressor,
        "LightGBM": lightgbm.LGBMRegressor,
        "RandomForest": RandomForestRegressor,
        "LinearRegression": LinearRegression,
        "Ridge": Ridge,
        "Lasso": Lasso,
        "ElasticNet": ElasticNet
    },
    "Clustering": {
        "KMeans": KMeans,
        "AgglomerativeClustering": AgglomerativeClustering,
        "DBSCAN": DBSCAN,
        "OPTICS": OPTICS
    },
    "Anomaly Detection": {
        "XGBoost": xgboost.XGBClassifier,
        "CatBoost": catboost.CatBoostClassifier,
        "LightGBM": lightgbm.LGBMClassifier,
        "RandomForest": RandomForestClassifier,
    }
}

st.title("Model")

st.write("Welcome to the model page")
st.write("you can create a model here")

st.write("## Choose problem type")
problem_type = st.selectbox("Problem type", ["Classification", "Regression", "Clustering", "Anomaly Detection"])

st.write("## Choose model type")
model_type = st.selectbox("Model type", problem_type_to_model_type_dict[problem_type])

with st.expander("Model description"):
    st.write(problem_specific_model_description_dict[problem_type][model_type])

st.write("## Choose parameters")
parameters = required_parameters_dict[problem_type][model_type]
hyperparameter_range = hyperparameter_range_dict[problem_type][model_type]
parameters_setting = {}
recommended,custum = st.tabs(["Recommended","Custom"])

with recommended:
    # use form to input parameters
    #when submit, save parameters to parameters_setting
    st.write("### Recommended parameters")
    for parameter in parameters:
        range_data , range_type = hyperparameter_range[parameter]
        if range_type == "list":
            parameters_setting[parameter] = st.selectbox(parameter, range_data)
        elif range_type == "bool":
            parameters_setting[parameter] = st.checkbox(parameter)
        elif range_type == "tuple":
            parameters_setting[parameter] = st.slider(parameter, range_data[0], range_data[1])

with custum:
    #user input parameters
    #using **parameters_setting to create model object
    st.write("### Custom parameters")
    st.write("Please input parameters with the following format:")
    st.write("``` parameter_name = parameter_value ```")
    st.write("For example:")
    st.write("``` objective = 'binary:logistic' ```")
    input_parameters = st.text_area("Input parameters")

if st.button("Submit"):
        st.json(parameters_setting)

st.write("## Create model")

st.write("### Model name")

model_name = st.text_input("Model name")
if model_name == "":
    st.warning("Please input model name")
    st.stop()
if os.path.isfile(f"models/{model_name}.pkl"):
    st.warning("Model name already exists")
    st.stop()

col1, col2 = st.columns(2)

model = None

with col1:
    if st.button("Create"):
        st.write("Save model")
        #save model to model folder
        model = model_dict[problem_type][model_type](**parameters_setting)
        st.write(model.get_params())
        st.success(f"Model {model_name} created")

with col2:
    if st.button("Save"):
        st.write(f"Path: {os.getcwd()}")
        #check if model folder exists
        if not os.path.isdir("models"):
            os.mkdir("models")
        with open(f"models/{model_name}.pkl", "wb") as f:
            pickle.dump(model, f)
        st.success(f"Model {model_name} saved!")
