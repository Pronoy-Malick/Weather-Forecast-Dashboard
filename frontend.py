import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="centered")
st.title("Weather Forecast for the next 5 days")
place = st.text_input("Place", placeholder="Enter the location")
days = st.slider("Number of Days", min_value=1, max_value=5)
option = st.selectbox("Choose Data to view", ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} in {place}")

if place:
    filtered_data =  get_data(place,days,option)
    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x= dates ,y= temperatures,labels={'x': 'Dates', 'y': 'Temperature(C)'})
        st.plotly_chart(figure)

    if option == "Sky":
