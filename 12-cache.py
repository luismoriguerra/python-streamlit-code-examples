import streamlit as st
from time import time

x = 200
y = 3000000
    
def non_cached_function(x, y):
    return x ** y

start = time()
non_cached_function(x, y)
duration = round((time() - start), 3)

st.write(f"Non-Cached Function took {duration} seconds to run")

@st.cache_data
def cached_function(x, y):
    return x ** y

start = time()
cached_function(x, y)
duration = round((time() - start), 3)

st.write(f"Cached Function took {duration} seconds to run")