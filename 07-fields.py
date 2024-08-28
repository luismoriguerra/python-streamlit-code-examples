import streamlit as st
import pandas as pd

st.button("Click button")

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Birds": ["Parrot", "Eagle", "Duck", "Pegeon", "Vulture"]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.button("Click to show only mammals"):
    st.dataframe(df["Mammals"])


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.checkbox("Click to add a check mark")

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Number": [5, 3, 7, 1, 6]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.checkbox("Click to show a graph of the data"):
    fig, ax = plt.subplots()
    ax = sns.barplot(x="Mammals", y="Number", data=df)
    st.pyplot(fig)
    

st.radio("Which of these is not a mammal?",
["Dog", "Cat", "Eagle", "Pig"])

st.selectbox("Which of these is a mammal?",
["Pigeon", "Dove", "Fox", "Vulture"])

st.select_slider("Which of these is not a bird?",
["Ostrich", "Flamingo", "Turkey", "Bat", "Pigeon"])

st.multiselect("Which of these are birds?",
["Fox", "Eagle",
"Bat", "Dove"])

slider_int = st.slider("Select an integer",
                       min_value=0,
                       max_value=100,
                       value=25)
st.write(slider_int, type(slider_int))

slider_float = st.slider("Select a float",
                         min_value=0.0,
                         max_value=100.0,
                         value=25.0)
st.write(slider_float, type(slider_float))