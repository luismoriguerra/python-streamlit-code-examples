import streamlit as st
import time

placeholder = st.empty()

placeholder.line_chart({"data": [1, 5, 2, 6]})
time.sleep(2)
#Replace the chart with several elements:
with placeholder.container():
    st.markdown("### This is one element within the container")
    time.sleep(2)
    st.markdown("### This is a second one, soon to be followed by an image")
    time.sleep(2)
    st.image("https://bit.ly/edus3ha")
    time.sleep(10)
#Clear all those elements:
placeholder.empty()