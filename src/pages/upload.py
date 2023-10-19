
from data import seaborn_datasets
from sklearn import datasets
from seaborn import load_dataset
from keras.datasets import mnist, fashion_mnist, cifar10, cifar100, imdb, reuters
from utl import dataset_df_config, dataset_np_config
import pandas as pd
import numpy as np
import streamlit as st
import yaml
import os

st.write("# Data Upload")

tab1, tab2, tab3, tab4 = st.tabs(["Upload", "Sklearn", "Seaborn", "Keras"])

config_yaml_path = 'datasets/config.yaml'
data_case = ""
df = None

def dataset_discrb(df):
    st.write("## Dataset Description")
    st.write("Dataset Head")
    st.write(df.head())
    st.write("Dataset Tail")
    st.write(df.describe())
    st.write("Dataset Data types")
    st.write(df.dtypes)
    st.write("Dataset Shape")
    st.write(df.shape)
    st.write("Dataset Columns")
    st.write(df.columns)
    st.write("Dataset Null Values")
    st.write(df.isnull().sum())

with tab1:
    st.write("## Upload Dataset")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        dataset_discrb(df)
        data_case = "df"

with tab2:
    st.write("## Sklearn Dataset")
    dataset_name_list = [dataset_name for dataset_name in dir(datasets) if dataset_name.startswith('load_')]
    dataset_name_list.remove("load_sample_images")
    dataset_name_list.remove("load_sample_image")
    dataset_name_list.remove("load_svmlight_file")
    dataset_name_list.remove("load_svmlight_files")
    sklearn_dataset = st.selectbox("Choose a dataset", dataset_name_list, index=None)
    if sklearn_dataset is not None:
        dataset = getattr(datasets, sklearn_dataset)()
        df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
        st.write(df)
        dataset_discrb(df)
        data_case = "df"

with tab3:
    st.write("## Seaborn Dataset")
    seaborn_dataset = st.selectbox("Choose a dataset", seaborn_datasets, index=None)
    if seaborn_dataset is not None:
        df = load_dataset(seaborn_dataset)
        st.write(df)
        dataset_discrb(df)
        data_case = "df"

with tab4:
    st.write("## Keras Dataset")
    dataset_name_list = ["mnist", "fashion_mnist", "cifar10", "cifar100", "imdb", "reuters"]
    keras_dataset = st.selectbox("Choose a dataset", dataset_name_list, index=None)
    if keras_dataset is not None:
        if keras_dataset == "mnist":
            (x_train, y_train), (x_test, y_test) = mnist.load_data()
        elif keras_dataset == "fashion_mnist":
            (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
        elif keras_dataset == "cifar10":
            (x_train, y_train), (x_test, y_test) = cifar10.load_data()
        elif keras_dataset == "cifar100":
            (x_train, y_train), (x_test, y_test) = cifar100.load_data()
        elif keras_dataset == "imdb":
            (x_train, y_train), (x_test, y_test) = imdb.load_data()
        elif keras_dataset == "reuters":
            (x_train, y_train), (x_test, y_test) = reuters.load_data()

        data_case = "np"
        with st.expander("keras dataset description"):
            st.write("Keras dataset is numpy array")
        

dataset_name = st.text_input("Dataset name")

button_trigger = st.button("Save")

if df is not None and button_trigger and dataset_name != "" and data_case == "df":
    print("df")
    #write basic info to yaml
    #if not exist, create
    state = dataset_df_config(dataset_name, config_yaml_path, f"datasets/{dataset_name}.csv", data_case, df)

    if state:
        st.success("Saved")
        st.info("Now you can go to Data Process page to process the dataset")

if data_case == "np" and button_trigger and dataset_name != "":
    print("np")
    state = dataset_np_config(dataset_name, config_yaml_path, f"datasets/{dataset_name}.npz", data_case, x_train, y_train, x_test, y_test)
    
    if state:
        st.success("Saved")
        st.info("Now you can go to Data Process page to process the dataset")