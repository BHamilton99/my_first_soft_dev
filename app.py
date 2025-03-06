# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('Data/diabetes_dataset.csv')

# Add a header
st.header("Diabetes Dataset Analysis")

# Create a histogram
st.subheader("Histogram of Age")
fig_hist = px.histogram(df, x='Age', title='Distribution of Age')
st.plotly_chart(fig_hist)

# Create a scatter plot
st.subheader("Scatter Plot: Age vs BMI")
fig_scatter = px.scatter(df, x='Age', y='BMI', title='Age vs BMI')
st.plotly_chart(fig_scatter)

# Add a checkbox to show/hide the dataset
if st.checkbox("Show Dataset"):
    st.write(df)
print(df.columns)
