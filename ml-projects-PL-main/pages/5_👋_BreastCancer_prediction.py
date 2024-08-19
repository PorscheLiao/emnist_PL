import streamlit as st
import joblib

# 載入模型與標準化轉換模型
clf = joblib.load('br_model.joblib')
scaler = joblib.load('br_scaler.joblib')

st.title('Breast Cancer預測')
radius_mean = st.slider('radius (mean):', min_value=6.981, max_value=28.11, value=11.00)
texture_mean = st.slider('texture (mean):', min_value=9.71, max_value=39.28, value=20.18)
perimeter_mean = st.slider('perimeter (mean):', min_value=43.79, max_value=188.5, value=60.0)
area_mean = st.slider('area (mean):', min_value=143.5, max_value=2501.0, value=1000.0)
smoothness_mean = st.slider('smoothness (mean):', min_value=0.053, max_value=0.163, value=0.1)
compactness_mean  = st.slider('compactness (mean):', min_value=2.0, max_value=5.0, value=3.5)
concavity_mean = st.slider('concavity (mean):', min_value=0.0, max_value=0.427, value=0.2)
concave_points_mean = st.slider('concave points (mean):', min_value=0.0, max_value=0.201, value=0.1)
symmetry_mean = st.slider('symmetry (mean):', min_value=0.106, max_value=0.304, value=0.2)
fractal_dimension_mean = st.slider('fractal dimension (mean):', min_value=0.05, max_value=0.097, value=0.07)

radius_error = st.slider('radius (standard error):', min_value=0.112, max_value=2.873, value=1.0)
texture_error = st.slider('texture (standard error):', min_value=0.36, max_value=4.885, value=2.0)
perimeter_error = st.slider('perimeter (standard error):', min_value=0.757, max_value=21.98, value=10.0)
area_error = st.slider('area (standard error):', min_value=6.802, max_value=542.2, value=200.0)
smoothness_error = st.slider('smoothness (standard error):', min_value=0.002, max_value=0.031, value=0.02)
compactness_error = st.slider('compactness (standard error):', min_value=0.002, max_value=0.135, value=0.01)
concavity_error = st.slider('concavity (standard error):', min_value=0.0, max_value=0.396, value=0.1)
concave_points_error = st.slider('concave points (standard error):', min_value=0.0, max_value=0.053, value=0.02)
symmetry_error = st.slider('symmetry (standard error):', min_value=0.008, max_value=0.079, value=0.01)
fractal_dimension_error = st.slider('fractal dimension (standard error):', min_value=0.001, max_value=0.03, value=0.01)

radius_worst = st.slider('radius (worst):', min_value=7.93, max_value=36.04, value=11.00)
texture_worst = st.slider('texture (worst):', min_value=12.02, max_value=49.54, value=20.0)
perimeter_worst = st.slider('perimeter (worst):', min_value=50.41, max_value=251.2, value=100.0)
area_worst = st.slider('area (worst):', min_value=185.2, max_value=4254.0, value=500.0)
smoothness_worst = st.slider('smoothness (worst):', min_value=0.071, max_value=0.223, value=0.2)
compactness_worst = st.slider('compactness (worst):', min_value=0.027, max_value=1.058, value=0.6)
concavity_worst = st.slider('concavity (worst):', min_value=0.0, max_value=1.252, value=0.6)
concave_points_worst = st.slider('concave points (worst):', min_value=0.0, max_value=0.291, value=0.1)
symmetry_worst = st.slider('symmetry (worst):', min_value=0.156, max_value=0.664, value=0.3)
fractal_dimension_worst = st.slider('fractal dimension (worst):', min_value=0.055, max_value=0.208, value=0.1)
labels = ['malignant','benign']
if st.button('預測'):
    X_new = [[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,
              radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,
              radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst, ]]
    X_new = scaler.transform(X_new)
    st.write('### Breast Cancer Prediction is：', labels[clf.predict(X_new)[0]])
