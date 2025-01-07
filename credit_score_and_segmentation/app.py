import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# App title
st.title("Credit Scoring and Segmentation App")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Load dataset
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Dataset")
    st.write(data.head())

    # Handle missing values
    if data.isnull().sum().sum() > 0:
        st.warning("The dataset contains missing values. Filling them with median values.")
        data = data.fillna(data.median())

    # Map categorical variables
    education_mapping = {'Master': 3, 'High School': 1, 'PhD': 4, 'Bachelor': 2}
    employment_mapping = {'Employed': 2, 'Unemployed': 1, 'Self-Employed': 3}
    
    if 'Education Level' in data.columns:
        data['Education Level'] = data['Education Level'].map(education_mapping)

    if 'Employment Status' in data.columns:
        data['Employment Status'] = data['Employment Status'].map(employment_mapping)

    # Calculate Credit Score
    if all(col in data.columns for col in ["Payment History", "Credit Utilization Ratio", "Number of Credit Accounts", "Education Level", "Employment Status"]):
        data['Credit Score'] = (
            0.35 * data['Payment History'] +
            0.30 * data['Credit Utilization Ratio'] +
            0.15 * data['Number of Credit Accounts'] +
            0.10 * data['Education Level'] +
            0.10 * data['Employment Status']
        )

        # Normalize Credit Score (Assume 0-1000 scale)
        data['Credit Score'] = (data['Credit Score'] / data['Credit Score'].max()) * 1000

        # Segmentation based on Credit Score
        def segment(score):
            if score >= 800:
                return 'Excellent'
            elif score >= 600:
                return 'Good'
            elif score >= 400:
                return 'Low'
            else:
                return 'Very Low'

        data['Segment'] = data['Credit Score'].apply(segment)

        # Display the dataset with Credit Score and Segment
        st.write("### Dataset with Credit Scores and Segments")
        st.write(data[['Credit Score', 'Segment']].head())

        # Visualization
        st.write("### Customer Segmentation Based on Credit Scores")
        fig = px.scatter(
            data,
            x=data.index,
            y='Credit Score',
            color='Segment',
            title="Customer Segmentation Based on Credit Scores",
            labels={"x": "Customer Index", "y": "Credit Score"},
            color_discrete_map={
                'Excellent': 'green',
                'Good': 'blue',
                'Low': 'red',
                'Very Low': 'yellow'
            }
        )
        st.plotly_chart(fig)
    else:
        st.error("The dataset must contain the following columns: 'Payment History', 'Credit Utilization Ratio', 'Number of Credit Accounts', 'Education Level', 'Employment Status'")
else:
    st.info("Please upload a CSV file to get started.")
