import streamlit as st

genre = st.radio(
    "你最喜歡的節目是什麼",
    ('卡通', '劇情', '紀錄片','我什麼都不喜歡'))
st.divider()
if genre == '卡通':
    st.write('你選擇卡通')

elif genre == "劇情":
    st.write("你選擇劇情")
elif genre == "紀錄片":
    st.write("你選紀錄片")
else:
    st.write("你是阿呆！")
st.divider()