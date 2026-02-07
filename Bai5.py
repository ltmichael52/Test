import streamlit as st

#python -m streamlit --version : kiểm tra phiên bản streamlit
#python -m streamlit run tenFile.py : chạy file python 
#Ctr+ C : dừng trang web 

st.title("First lesson in streamlit")
st.write("Xin chào")
st.write("Today is saturday")

hobbies = st.text_input("Sở thích của bạn là gì? ")
st.write("Sớ thích của bạn là: ",hobbies)