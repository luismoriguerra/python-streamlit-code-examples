import streamlit as st
import time

# with st.spinner("Counting on going..."):
#     progress_bar = st.progress(0)
#     for done in range(100):
#         time.sleep(0.1)
#         progress_bar.progress(done + 1)    
# st.success("Counting complete.")
# st.balloons()

st.error("Syntax error")

st.exception(ZeroDivisionError("Divide by zero error"))

st.warning("This will be deprecated soon")

st.info("App running optimally")