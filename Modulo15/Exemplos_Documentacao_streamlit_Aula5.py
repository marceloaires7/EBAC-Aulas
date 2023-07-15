import numpy as np
import streamlit as st

st.write("Hello, World!")

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)