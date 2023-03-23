import streamlit as st
import pickle
import pandas as pd
st.set_page_config(page_title='Health Bridge', initial_sidebar_state='auto')

st.markdown("# Diabetes prediction model")
checks = st.columns(4)
data = list()
if st.checkbox('Age'):
    data.append('Age')
if st.checkbox('Gender'):
    data.append('Gender')
if st.checkbox('Polyuria'):
    data.append('Polyuria')
if st.checkbox('Polydipsia'):
    data.append('Polydipsia')
if st.checkbox('sudden weight loss'):
    data.append('sudden weight loss')
if st.checkbox('weakness'):
    data.append('weakness')
if st.checkbox('Polyphagia'):
    data.append('Polyphagia')
if st.checkbox('Genital thrush'):
    data.append('Genital thrush')
if st.checkbox('visual blurring'):
    data.append('visual blurring')
if st.checkbox('Itching'):
    data.append('Itching')
if st.checkbox('Irritability'):
    data.append('Irritability')
if st.checkbox('delayed healing'):
    data.append('delayed healing')
if st.checkbox('partial paresis'):
    data.append('partial paresis')
if st.checkbox('muscle stiffness'):
    data.append('muscle stiffness')
if st.checkbox('Alopecia'):
    data.append('Alopecia')
if st.checkbox('Obesity'):
    data.append('Obesity')

if st.button('Predict'):
    diagonosis_model = pickle.load(open('models/telemedicine_model', 'rb'))
    csv_file = "../assets/diabetes_model"
    df = pd.read_csv(csv_file)