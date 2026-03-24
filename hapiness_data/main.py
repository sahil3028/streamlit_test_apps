import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search of Happiness")

df = pd.read_csv('hapiness_data/data/happy.csv')

numeric_cols = df.select_dtypes(include='number').columns

x_axis = st.selectbox("Select X-axis", numeric_cols)
y_axis = st.selectbox("Select Y-axis", numeric_cols)

fig = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(fig)