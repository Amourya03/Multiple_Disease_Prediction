import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           icons=['activity', 'heart'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPredigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Validate and convert inputs to numeric
    try:
        Pregnancies = float(Pregnancies) if Pregnancies else None
        Glucose = float(Glucose) if Glucose else None
        BloodPressure = float(BloodPressure) if BloodPressure else None
        SkinThickness = float(SkinThickness) if SkinThickness else None
        Insulin = float(Insulin) if Insulin else None
        BMI = float(BMI) if BMI else None
        DiabetesPredigreeFunction = float(DiabetesPredigreeFunction) if DiabetesPredigreeFunction else None
        Age = float(Age) if Age else None
    except ValueError:
        st.error("Please enter valid numeric values for all input fields.")
        st.stop()

    # creating a button for Prediction
    button_clicked = st.button('Diabetes Test Result')

    # code for Prediction
    if button_clicked and all(val is not None for val in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]])

        if diab_prediction[0] == 1:
            st.success('The person is Diabetic')
        else:
            st.success('The person is not Diabetic')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain Types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal:0=normal; 1=fixed defect; 2=reversal defect')

    # Validate and convert inputs to numeric
    try:
        age = float(age) if age else None
        sex = float(sex) if sex else None
        cp = float(cp) if cp else None
        trestbps = float(trestbps) if trestbps else None
        chol = float(chol) if chol else None
        fbs = float(fbs) if fbs else None
        restecg = float(restecg) if restecg else None
        thalach = float(thalach) if thalach else None
        exang = float(exang) if exang else None
        oldpeak = float(oldpeak) if oldpeak else None
        slope = float(slope) if slope else None
        ca = float(ca) if ca else None
        thal = float(thal) if thal else None
    except ValueError:
        st.error("Please enter valid numeric values for all input fields.")
        st.stop()

    # creating a button for Prediction
    button_clicked_heart = st.button('Heart Disease Test Result')

    # code for Prediction
    if button_clicked_heart and all(val is not None for val in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            st.success('The person is having Heart Disease')
        else:
            st.success('The person does not have Heart Disease')
