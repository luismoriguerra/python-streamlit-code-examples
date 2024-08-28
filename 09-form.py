import streamlit as st

number = st.sidebar.slider("Choose a number",
                           min_value=-1.0,
                           max_value=1.0,)

st.metric("Selected number", number)

import streamlit as st

with st.form("Order Form"):
    st.write("Order Details")
    fruit = st.select_slider("Select a fruit",
                             ["Banana", "Pawpaw", "Guava", "Mango"])

    quantity = st.number_input("Select the number of fruits", min_value=0)

    city = st.text_input("Type in your city")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("You have ordered {} {}(s) to be picked up at the {} branch"
                 .format(quantity, fruit, city))

st.write("These values, {}, {}, and {}, that were set inside the form are\
         accessible outside the form".format(quantity, fruit, city))