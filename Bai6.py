import streamlit as st
import time

st.title("Bài 6")
name = st.text_input("Hãy nhập tên của bạn")

if st.button("Xác nhận"):
    st.write("Chào bạn: ",name)

st.button("Click me",1)
st.button("Click me",2)

st.progress(30)
progressBar = st.progress(0)

for i in range(100):
    time.sleep(0.05)
    progressBar.progress(i+1)

if st.button("Xuất hiện bong bóng "):
    st.balloons()

# git init : khởi tạo
# git remote add origin <URL> : thêm liên kết với remote repo <URL>
# git add . : thêm tất cả file vào stage 
# git add <tenfile> : thêmm file đó vào stage
# git commit -m "ABC" : thêm message
# git push origin <branch> : đẩy code lên github vô nhánh nào