import streamlit as st
import plotly.express as px

st.set_page_config(layout="centered")
st.title("Weather Forecast for the next 5 days")
place = st.text_input("Place", placeholder="Enter the location")
days = st.slider("Number of Days", min_value=1, max_value=5)
option = st.selectbox("Choose Data to view", ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} in {place}")

dates = ["20.04.2025","21.04.2025","22.04.2025"]
temperature = [10,20,8]

figure = px.line(x= dates ,y= temperature,labels={'x': 'Dates', 'y': 'Temperature(C)'})
st.plotly_chart(figure)