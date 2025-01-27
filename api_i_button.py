import streamlit as st
import pandas as pd
import numpy as np

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="primary"):
    st.write("Ciao")

st.divider()
 
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    })

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv",
)
text_contents = '''This is some text'''
st.download_button("Download some text", text_contents)


binary_contents = b"example content"
# Defaults to "application/octet-stream"
st.download_button("Download binary file", binary_contents)

st.divider()
st.link_button("Go to gallery", "https://streamlit.io/gallery")

st.divider()


st.page_link("pages/api_col.py", label="Home", icon="🏠")
st.page_link("pages/api_data.py", label="Page 1", icon="1️⃣")
st.page_link("pages/api_text.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")