'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-01-02 18:41:44
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-01-02 20:57:17
FilePath: \hayabusa\src\pages\data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import streamlit as st
import pandas as pd
import plotly.express as px
from utl import datasets_update

st.title('Data')

st.subheader('Upload Data')
data = st.file_uploader('Upload your data here', type=['csv', 'xlsx'])
if data is not None:
    st.success('Your data has been uploaded')
    st.subheader('Data Preview')
    df = pd.read_csv(data)

    st.dataframe(df.head(5))

    st.subheader('Data Description')
    st.write(df.describe())

    st.subheader('Data Visualization')
    all_columns = [col for col in df.columns if df[col].dtype == 'float64' or df[col].dtype == 'int64']
    type_of_plot = st.selectbox('Select Type of Plot', ['area', 'bar', 'line', 'hist', 'box'])
    selected_columns = st.multiselect('Select Columns To Plot', all_columns)

    if st.button('Generate Plot'):
        st.success('Generating Customizable Plot of {} for {}'.format(type_of_plot, selected_columns))

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

    st.subheader('Save Data')
    file_name = st.text_input('Enter File Name')
    password = st.text_input('Enter Password', type='password', key='password_2')
    if st.button('Save Data'):
        if password != None:
            df.to_csv('./datasets/{}.csv'.format(file_name), index=False)
            datasets_update('{}.csv'.format(file_name),password)
            st.success('Your data has been saved')
        elif password == None:
            st.warning('Please enter password')
        elif file_name == None:
            st.warning('Please enter file name')