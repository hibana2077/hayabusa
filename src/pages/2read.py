import streamlit as st
import os
import pandas as pd
import plotly.express as px
from utl import datasets_read

st.title('Read Data')

st.subheader('Select Data')

file_list = os.listdir('./datasets')
file_list = [file for file in file_list if file.endswith('.csv')]


with st.form(key='read_data'):
    file_list = st.selectbox('Select Data', file_list)
    password = st.text_input('Enter Password', type='password', key='password_1')
    submit = st.form_submit_button('Read Data')

    if submit:
        st.success('Data Read Successfully')
        st.session_state['file_list'] = file_list
        st.session_state['password'] = password
        st.rerun()

if 'file_list' in st.session_state and 'password' in st.session_state:
    file_list = st.session_state['file_list']
    password = st.session_state['password']
    df = datasets_read(file_list, password)
    st.subheader('Data Preview')
    st.dataframe(df.head(5))

    st.subheader('Data Description')
    st.write(df.describe())

    st.subheader('Data Visualization')
    all_columns = [col for col in df.columns if df[col].dtype == 'float64' or df[col].dtype == 'int64']
    type_of_plot = st.selectbox('Select Type of Plot', ['area', 'bar', 'line', 'hist', 'box'])
    selected_columns = st.multiselect('Select Columns To Plot', all_columns)

    if type_of_plot == 'area':
        cust_data = df[selected_columns]
        st.area_chart(cust_data)

    elif type_of_plot == 'bar':
        cust_data = df[selected_columns]
        st.bar_chart(cust_data)

    elif type_of_plot == 'line':
        cust_data = df[selected_columns]
        st.line_chart(cust_data)

    elif type_of_plot == 'hist':
        cust_data = df[selected_columns]
        fig = px.histogram(cust_data, x=selected_columns)
        st.plotly_chart(fig)

    elif type_of_plot == 'box':
        cust_data = df[selected_columns]
        fig = px.box(cust_data, x=selected_columns)
        st.plotly_chart(fig)