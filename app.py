# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('placement.pkl', 'rb'))

# Sidebar: project description
st.sidebar.title("About This Project")
st.sidebar.info("""
This Job Placement Prediction app helps HR professionals and students estimate the likelihood of a candidate being placed based on academic performance and skills.  

**Benefits:**
- Quick assessment of candidates
- Data-driven decision making
- Helps identify areas for improvement
""")

st.title("Job Placement Prediction")
st.write("Enter the candidate's details:")

# Use columns for two-input layout
col1, col2 = st.columns(2)

with col1:
    ssc_percentage = st.number_input("SSC Percentage", 0.0, 100.0, 67.0)
with col2:
    hsc_percentage = st.number_input("HSC Percentage", 0.0, 100.0, 70.0)

with col1:
    degree_percentage = st.number_input("Degree Percentage", 0.0, 100.0, 65.0)
with col2:
    etest_percentage = st.number_input("E-Test Percentage", 0.0, 100.0, 88.0)

with col1:
    mba_percentage = st.number_input("MBA Percentage", 0.0, 100.0, 71.96)
with col2:
    gender_male = st.selectbox("Gender (Male=1, Female=0)", [0, 1])

with col1:
    ssc_board_other = st.selectbox("SSC Board (Other=1, Central=0)", [0, 1])
with col2:
    hsc_board_other = st.selectbox("HSC Board (Other=1, Central=0)", [0, 1])

with col1:
    hsc_subject_Commerce = st.selectbox("HSC Subject (Commerce=1, Science=0)", [0, 1])
with col2:
    undergrad_BBA = st.selectbox("Undergrad Degree BBA=1, BTech=0, Other=0", [0, 1])

with col1:
    undergrad_BTech = st.selectbox("Undergrad Degree BTech=1, BBA/Other=0", [0, 1])
with col2:
    work_experience_yes = st.selectbox("Work Experience (Yes=1, No=0)", [0, 1])

with col1:
    specialisation_MktTech = st.selectbox("Specialisation Mkt & Tech=1, Mkt & Rural=0", [0, 1])
with col2:
    specialisation_MktRural = st.selectbox("Specialisation Mkt & Rural=1, Mkt & Tech=0", [0, 1])

# Predict Button
if st.button("Predict Placement"):
    input_data = (
        ssc_percentage, hsc_percentage, degree_percentage, etest_percentage, mba_percentage,
        gender_male, ssc_board_other, hsc_board_other, hsc_subject_Commerce,
        undergrad_BBA, undergrad_BTech, work_experience_yes, specialisation_MktTech, specialisation_MktRural
    )
    
    np_input = np.array(input_data).reshape(1, -1)
    prediction = model.predict(np_input)
    
    if prediction[0] == 1:
        st.success("✅ This person is placed for the job")
    else:
        st.error("❌ This person is not placed for the job")
