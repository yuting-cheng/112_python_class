import streamlit as st

"我上課不睡覺"
agree = st.checkbox('我同意') #預設為fasls 

if agree:
    st.write('Great!')