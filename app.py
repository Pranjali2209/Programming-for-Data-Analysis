import streamlit as st
from nbconvert import HTMLExporter
import nbformat
import pickle
import pandas as pd

# Custom CSS for red theme
st.markdown("""
    <style>
        body {
            background-color: #FFEBEE;
        }
        .sidebar .sidebar-content {
            background-color: #FFCDD2;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #B71C1C;
        }
        .stButton button {
            background-color: #E57373;
            color: white;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            background-color: #FFCDD2;
        }
        .stMarkdown p {
            color: #D32F2F;
        }
        .stDataFrame {
            border: 1px solid #B71C1C;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Data Overview", "EDA", "Model"])

# EDA Page
if page == "EDA":
    st.title("Exploratory Data Analysis")

    st.markdown("1. PM2.5")
    st.image('pm2.5.png')
    
    st.markdown("2. PM10")
    st.image('PM10.png')

    st.markdown("3. DEWP")
    st.image('dewp.png')

    st.markdown("4. station")
    st.image('station.png')

    st.markdown("5. TEMP")
    st.image('temp.png')

# Model Page
elif page == "Model":
    st.title("Model Prediction Page")
    
    def predict(model, input_data):
        prediction = model.predict(input_data)
        return prediction[0]

    st.title("Temperature Prediction")

    # Input fields for the features
    month = st.selectbox("Month", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    day = st.slider('Day', 0, 31)
    hour = st.slider('Hour', 0, 24)
    O3 = st.number_input("O3", min_value=0.2, max_value=1071.0, step=0.1)
    DEWP = st.number_input("Dew Point (DEWP)", min_value=-43.4, max_value=29.1)
    RAIN = st.number_input("Rain", min_value=0.0, max_value=72.5, step=0.1)
    wd = st.selectbox("wd", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    WSPM = st.number_input("Wind Speed (WSPM)", min_value=0.0, max_value=13.2, step=0.1)

    input_data = pd.DataFrame({
        'month': [month],
        'day': [day],
        'hour': [hour],
        'O3': [O3],
        'DEWP': [DEWP],
        'RAIN': [RAIN],
        'wd': [wd],
        'WSPM': [WSPM],
    })

    model_choice = st.selectbox("Select model for prediction", ("KNN Regressor", ""))

    predi = 0.90
    if model_choice == "Random Forest Regressor":
        forest = pickle.load(open('forest.pkl', 'rb'))
        predi = predict(forest, input_data)
    elif model_choice == "KNN Regressor":
        knn = pickle.load(open('knn.pkl', 'rb'))
        predi = predict(knn, input_data)
        predi = predi[0]
    elif model_choice == "Linear Regressor":
        lr = pickle.load(open('lr.pkl', 'rb'))
        predi = predict(lr, input_data)
        predi = predi[0]
    elif model_choice == "Decision Tree Regressor":
        dtc = pickle.load(open('tree.pkl', 'rb'))
        predi = predict(dtc, input_data)

    st.subheader(f"Predicted Temperature is: {round(predi, 2)}")
