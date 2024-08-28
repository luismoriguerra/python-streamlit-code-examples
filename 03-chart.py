import streamlit as st
import numpy as np

df = np.random.randn(5,5)

c1, c2, c3 = st.columns(3)

with c1:
	st.markdown("## Line Chart")
	st.line_chart(df)
with c2:
	st.markdown("## Area Chart")
	st.area_chart(df)
with c3:
	st.markdown("## Bar Chart")
	st.bar_chart(df)	

    
arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)

import matplotlib.pyplot as plt
import seaborn as sns

arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)

c1, c2 = st.columns(2)

with c1:
	fig, ax = plt.subplots()
	ax.set_title("Matplotlib Scatter Plot")
	ax.scatter(arr1, arr2, s = arr3, c = arr3, alpha = 0.6)
	st.pyplot(fig)

with c2:
	fig, ax = plt.subplots()
	ax.set_title("Seaborn Scatter Plot")
	ax = sns.scatterplot(x=arr1, y=arr2)
	st.pyplot(fig)


import plotly.express as px

arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)

fig = px.scatter(x=arr1, y=arr2, title="Plotly Scatter Plot")
st.plotly_chart(fig, use_container_width=True)
