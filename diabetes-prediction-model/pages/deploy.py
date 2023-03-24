import streamlit as st
import pickle
import pandas as pd
import csv
st.set_page_config(page_title='Health Bridge', initial_sidebar_state='auto')

data = pd.read_csv("assets/diabetes.csv")
headings = data.columns.to_list()
headings.remove("class")

csv_write = ['No']*16

st.markdown("# Diabetes prediction model")
checks = st.columns(4)
data = list()
if st.checkbox('Age'):
    data.append(0)
if st.checkbox('Gender'):
    data.append(1)
if st.checkbox('Polyuria'):
    data.append(2)
if st.checkbox('Polydipsia'):
    data.append(3)
if st.checkbox('sudden weight loss'):
    data.append(4)
if st.checkbox('weakness'):
    data.append(5)
if st.checkbox('Polyphagia'):
    data.append(6)
if st.checkbox('Genital thrush'):
    data.append(7)
if st.checkbox('visual blurring'):
    data.append(8)
if st.checkbox('Itching'):
    data.append(9)
if st.checkbox('Irritability'):
    data.append(10)
if st.checkbox('delayed healing'):
    data.append(11)
if st.checkbox('partial paresis'):
    data.append(12)
if st.checkbox('muscle stiffness'):
    data.append(13)
if st.checkbox('Alopecia'):
    data.append(14)
if st.checkbox('Obesity'):
    data.append(15)

if st.button('Predict'):
    st.write(data)
    with open("../prediction.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headings)
        for i in range(len(headings)):
            if 