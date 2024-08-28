import streamlit as st
import pandas as pd
integer_number = st.number_input("Enter an integer",
                                 min_value=-10,
                                 max_value=10,
                                 value=0)
st.write(integer_number, type(integer_number))

float_number = st.number_input("Enter a float",
                               min_value=-1.0,
                               max_value=1.0,
                               value=0.0)
st.write(float_number, type(float_number))

st.markdown("## Single-Line Input")
text_input = st.text_input("Give an example of a mammal")
st.write(text_input)

st.markdown("## Multi-Line Input")
text_area = st.text_area("Give a list of 3 birds")
st.write(text_area)

st.markdown("## Files")
file = st.file_uploader("Select a file to upload", type=["png", "jpg"])

if file is not None:
    st.image(file)

st.markdown("## File dowloading")
df = pd.DataFrame({"Mammal": ["Cat", "Bat", "Fox"],
                   "Number": [3, 1, 5]})

st.dataframe(df)

st.download_button("Download data",
                   df.to_csv(index=False),
                   file_name="data.csv")
