import streamlit as st

if st.button("Home"):
    st.switch_page("api_nav.py")
if st.button("Page 1"):
    st.switch_page("pages/api_col.py")
if st.button("Page 2"):
    st.switch_page("pages/api_data.py")