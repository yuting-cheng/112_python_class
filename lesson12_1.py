import streamlit as st
import pandas as pd

codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str) + codeFrame['name']

with st.sidebar:
    selected_code = st.multiselect("請選擇股票(可複選):",codeSeries,max_selections=4)



for code in selected_code:
    code = code[:4]+'.TW' #此為取code前四位字＋TW 顯示
    st.write(code)