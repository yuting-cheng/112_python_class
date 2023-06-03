import streamlit as st

option = st.selectbox(
    '你想要如何聯絡我?',
    ('Email', '家裡電話', '我的手機'))

st.write('你的選擇：', option)