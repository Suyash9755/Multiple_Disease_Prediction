# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:32:45 2026

@author: suyas
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pickle  # Essential for loading .sav files
import os

# Get the directory where this script is saved
working_dir = os.path.dirname(os.path.abspath(__file__))

# Join the path to the 'saved models' folder
# Use forward slashes (/) or os.path.join for compatibility
diabetes_model = pickle.load(open(os.path.join(working_dir, 'saved models', 'daibetes_model.sav'), 'rb'))
breast_cancer_model = pickle.load(open(os.path.join(working_dir, 'saved models', 'breast_cancer_model.sav'), 'rb'))
heart_model = pickle.load(open(os.path.join(working_dir, 'saved models', 'heart_health.sav'), 'rb'))


# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Breast Cancer Prediction',
                            'Heart Health Prediction'],
                           icons=['activity', 'balloon', 'suit-heart'],
                           default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Pregnancies')
        Glucose = st.text_input('Glucose')
        BloodPressure = st.text_input('Blood Pressure')
    with col2:
        SkinThickness = st.text_input('Skin Thickness')
        Insulin = st.text_input('Insulin')
        BMI = st.text_input('BMI')
    with col3:
        DiabetesPedigreeFunction = st.text_input('DPF Value')
        Age = st.text_input('Age')
        
    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        #  Convert inputs to float so the model can process them
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]# Basic error handling for empty fields

        #  Prediction
        diab_pred = diabetes_model.predict([user_input])
        
        if diab_pred[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
            st.error(diab_diagnosis) # Red box for positive results
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            st.success(diab_diagnosis) # Green box for negative results

# Placeholder logic for other pages
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction Using ML')
    # creating columns for input
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = st.text_input('radius mean')
        texture_mean = st.text_input('texture mean')
        perimeter_mean = st.text_input(' perimeter mean ')
        area_mean = st.text_input('area mean')
        smoothness_mean = st.text_input('smoothness mean')   
        compactness_mean = st.text_input('compactness mean')
        concavity_mean = st.text_input('concavity mean')
        concave_points_mean = st.text_input('concave points mean')
        symmetry_mean = st.text_input(' symmetry mean ')
        fractal_dimension_mean = st.text_input('fractal dimension mean')
        
    with col2:
        radius_se = st.text_input('radius se')
        texture_se = st.text_input('texture se')
        perimeter_se = st.text_input('perimeter se')
        area_se = st.text_input('area se')
        smoothness_se = st.text_input('smoothness se')
        compactness_se = st.text_input('compactness se')   
        concavity_se = st.text_input('concavity se')
        concave_points_se = st.text_input('concave points se')
        symmetry_se = st.text_input('symmetry se')
        fractal_dimension_se = st.text_input(' fractal dimension se ')
        
    with col3:
        radius_worst = st.text_input('radius worst')
        texture_worst = st.text_input('texture worst')
        perimeter_worst = st.text_input('perimeter worst')
        area_worst = st.text_input('area worst')
        smoothness_worst = st.text_input('smoothness worst')
        compactness_worst = st.text_input('compactness worst')   
        concavity_worst = st.text_input('concavity worst')
        concave_points_worst = st.text_input('concave points worst')   
        symmetry_worst = st.text_input('symmetry worst')
        fractal_dimension_worst = st.text_input('fractal dimension worst')
        
    breast_cancer = ' '
    
    if st.button('Breast Cancer Test Result'):
        #  Gather all user inputs
        user_input = [
            radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, 
            compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
            radius_se, texture_se, perimeter_se, area_se, smoothness_se, 
            compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
            radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, 
            compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
        ]
        
        
            # Convert to float
        numeric_input = [float(x) if x.strip() else 0.0 for x in user_input]
          # predict 
        brst_pred = breast_cancer_model.predict([numeric_input])
            
        if brst_pred[0] == 1:
            st.error('The tumor is Malignant (Cancerous)')
        else:
            st.success('The tumor is Benign (Non-Cancerous)')
                
       
        

if selected == 'Heart Health Prediction':
    st.title('Heart Health Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age')
        sex = st.text_input('sex')
        cp = st.text_input(' cp ')
        trestbps = st.text_input('trestbps')
    with col2:
        chol = st.text_input('chol')
        fbs = st.text_input('fbs')
        restecg = st.text_input('restecg')
        thalach = st.text_input('thalach')
    with col3:
        exang = st.text_input('exang')
        oldpeak = st.text_input('oldpeak')
        slope = st.text_input('slope')
        ca = st.text_input('ca')   
        thal = st.text_input('thal')
    
    heart_health = ' '
    
    if st.button('Heart Test Result'):
    # inoput
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    #  Convert to float
        numeric_input = [float(x) if x.strip() else 0.0 for x in user_input]

    #  Predict
        heart_pred = heart_model.predict([numeric_input])
    
        if heart_pred[0] == 1:
            st.error('The person has Heart Disease')
        else:
            st.success('The person has a Healthy Heart')