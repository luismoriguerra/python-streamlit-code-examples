import streamlit as st
import pandas as pd

st.metric(label="Velocity in kilometres per hour", value=75.4, delta=-2)

sample_data = {"Mammals": ["Cat", "Dog", "Pig"]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

st.table(df)

st.json(sample_data)

c1, c2 = st.columns(2)

with c1:
	st.markdown("## Metric")
	st.metric(label="Velocity in kilometres per hour", value=75.4, delta=-2)
	st.markdown("## Table")
	st.table(df)
with c2:
	st.markdown("## Dataframe")
	st.dataframe(df)
	st.markdown("## JSON")
	st.json(sample_data)
