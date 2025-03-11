# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("Data/diabetes_dataset.csv")

# Add a header
st.header("Diabetes Dataset Analysis")

# Sidebar for app controls
st.sidebar.header("Controls")

# Feature selection for scatter plot
x_column = st.sidebar.selectbox(
    "Select X-axis for scatter plot:",
    df.select_dtypes(include=["float", "int"]).columns.tolist(),
    index=df.columns.get_loc("Age") if "Age" in df.columns else 0
)
y_column = st.sidebar.selectbox(
    "Select Y-axis for scatter plot:",
    df.select_dtypes(include=["float", "int"]).columns.tolist(),
    index=df.columns.get_loc("BMI") if "BMI" in df.columns else 0
)

# Create the scatter plot based on selected features
st.subheader(f"Scatter Plot: {x_column} vs {y_column}")
fig_scatter = px.scatter(df, x=x_column, y=y_column, title=f'{x_column} vs {y_column}')
st.plotly_chart(fig_scatter)

# Create a histogram for Age
st.subheader("Histogram of Age")
fig_hist = px.histogram(df, x='Age', title='Distribution of Age')
st.plotly_chart(fig_hist)

# Add a checkbox to show/hide the dataset
if st.checkbox("Show Dataset"):
    st.write(df)

# Add a checkbox to show column names
if st.checkbox("Show Column Names"):
    st.write("Dataset Columns:", df.columns.tolist())

# Add a section for summary statistics
st.subheader("Dataset Summary Statistics")
if st.checkbox("Show Summary Statistics"):
    st.write(df.describe())
