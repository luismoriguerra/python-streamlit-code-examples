import streamlit as st

delta = None
step = 0.5

humidity = 75.0

raise_humidity = st.button("Raise humidity")
if raise_humidity:
    humidity += step
st.metric("The humidity is: ", humidity, delta)

if "temperature" not in st.session_state:
    st.session_state["temperature"] = 25.0

raise_temperature = st.button("Raise temperature")
if raise_temperature:
    st.session_state["temperature"] += step
    delta = step
lower_temperature = st.button("Lower temperature")
if lower_temperature:
    st.session_state["temperature"] -= step
    delta = -step

st.metric("The temperature is: ", st.session_state["temperature"], delta)