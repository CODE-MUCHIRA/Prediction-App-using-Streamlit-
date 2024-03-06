import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("D:\Azubi LP4\Prediction-Attrition-App\LP2_Telco-churn-last-2000 (2).csv")

# Show data table
st.write("## Data Table")
st.write(data)

# Visualizations
st.write("## Visualizations")

# Visualization 1: Histogram
st.write("### Histogram")
fig_hist, ax_hist = plt.subplots()
ax_hist.hist(data['MonthlyCharges'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('MonthlyCharges')
plt.ylabel('Frequency')
st.pyplot(fig_hist)

# Visualization 2: Scatter plot
st.write("### Scatter Plot")
fig_scatter, ax_scatter = plt.subplots()
ax_scatter.scatter(data['gender'], data['TotalCharges'], color='green')
plt.xlabel('gender')
plt.ylabel('TotalCharges')
st.pyplot(fig_scatter)

# Visualization 3: Bar chart
st.write("### Bar Chart")
age_counts = data['SeniorCitizen'].value_counts().sort_index()
fig_bar, ax_bar = plt.subplots()
ax_bar.bar(age_counts.index, age_counts.values, color='orange')
plt.xlabel('SeniorCitizen')
plt.ylabel('Count')
st.pyplot(fig_bar)