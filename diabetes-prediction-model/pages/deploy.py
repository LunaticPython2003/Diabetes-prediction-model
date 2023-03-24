import streamlit as st
import pickle
import pandas as pd
import csv
import os
st.set_page_config(page_title='Health Bridge', initial_sidebar_state='auto')

data = pd.read_csv("assets/diabetes.csv")
headings = data.columns.to_list()
headings.remove("class")

st.markdown("# Diabetes prediction model")
checks = st.columns(4)
data = [0]*15
age = st.slider("Your Age", 1, 70)
data[0] = age

option = st.selectbox(
    "Select your gender",
    ('Gender','Male', 'Female'))

if option == 'Male':
    option = 1
else:
    option = 0

if st.checkbox('Polyuria'):
    data[2]=1
if st.checkbox('Polydipsia'):
    data[3]=1
if st.checkbox('sudden weight loss'):
    data[4]=1
if st.checkbox('weakness'):
    data[5]=1
if st.checkbox('Polyphagia'):
    data[6]=1
if st.checkbox('Genital thrush'):
    data[7]=1
if st.checkbox('visual blurring'):
    data[8]=1
if st.checkbox('Itching'):
    data[9]=1
if st.checkbox('Irritability'):
    data[10]=1
if st.checkbox('delayed healing'):
    data[11]=1
if st.checkbox('partial paresis'):
    data[12]=1
if st.checkbox('muscle stiffness'):
    data[13]=1
if st.checkbox('Alopecia'):
    data[14]=1
if st.checkbox('Obesity'):
    data[15]=1

if st.button('Predict'):
    write_data = [age] + [0]*16
    data[1] = option
    for i in range(2, len(data)):
        if data[i] == 1:
            write_data[i] = 1
    write_data.pop()
    with open("prediction.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headings)
        writer.writerow(write_data)
    csv_file = "prediction.csv"
    diabetes = pd.read_csv(csv_file)

    diabetes_model = pickle.load(open('assets/diabetes_model', 'rb'))
    predictions = diabetes_model.predict(diabetes)

    if predictions[0]:
        st.markdown("## You are suffering from diabetes")
    else:
        st.markdown("## Congratulations, you are not suffering from diabetes!")

    os.remove("prediction.csv")