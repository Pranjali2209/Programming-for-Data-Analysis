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

