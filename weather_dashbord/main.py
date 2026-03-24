import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast app")
place=st.text_input("place: ")
days=st.slider("Forecast Days", min_value=1,max_value=5,help="no of days")
option=st.selectbox("select data to view",
                    ("temperature","sky"))

if place:



    if option=="temperature":
        d, t = get_data(place, days, option)
        if d is None:
            st.error("City not found. Try again.")
        else:
            st.subheader(f"{option} for the next {days} days in {place}")
            figure=px.line(x=d,y=t,labels={"x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)

    else:
        date,sky=get_data(place,days,option)
        if date is None:
            st.error("City not found. Try again.")
        else:
            st.subheader(f"{option} for the next {days} days in {place}")
            st.image(sky,width=115,caption=date)