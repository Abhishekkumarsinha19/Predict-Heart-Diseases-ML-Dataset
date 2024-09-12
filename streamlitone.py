import streamlit as st
import joblib
import numpy as np

# Load the trained model
loaded_model=joblib.load(r"C:\Users\hp\ML file\best_model.pkl")

# Streamlit app
st.title('CHD Risk Prediction')

# Create input fields for all 15 features
male = st.selectbox('Gender (0 = Female, 1 = Male)', [0, 1])
age = st.number_input('Age', min_value=20, max_value=100)
education = st.selectbox('Education Level (1, 2, 3, 4)', [1, 2, 3, 4])
currentSmoker = st.selectbox('Current Smoker (0 = No, 1 = Yes)', [0, 1])
cigsPerDay = st.number_input('Cigarettes per Day', min_value=0, max_value=100)
BPMeds = st.selectbox('On BP Medication (0 = No, 1 = Yes)', [0, 1])
prevalentStroke = st.selectbox('Prevalent Stroke (0 = No, 1 = Yes)', [0, 1])
prevalentHyp = st.selectbox('Prevalent Hypertension (0 = No, 1 = Yes)', [0, 1])
diabetes = st.selectbox('Diabetes (0 = No, 1 = Yes)', [0, 1])
totChol = st.number_input('Total Cholesterol', min_value=100, max_value=400)
sysBP = st.number_input('Systolic BP', min_value=80, max_value=200)
diaBP = st.number_input('Diastolic BP', min_value=60, max_value=130)
BMI = st.number_input('BMI', min_value=10.0, max_value=50.0)
heartRate = st.number_input('Heart Rate', min_value=50, max_value=150)
glucose = st.number_input('Glucose Level', min_value=50, max_value=300)

# Prediction button
if st.button('Predict'):
    # Collect all input data in the expected format (15 features)
    input_data = np.array([[male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp,
                            diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]])
    
    # Make prediction
    prediction = loaded_model.predict(input_data)
    
    # Display result
    if prediction[0] == 1:
        st.write('High risk of CHD in 10 years')
    else:
        st.write('Low risk of CHD in 10 years')
