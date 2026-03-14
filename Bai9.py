import streamlit as st

col1 , col2 ,col3,col4,col5 ,col6 = st.columns(6)

subCol1 , subCol2 = st.columns([2,1])

with col1:
    b1 = st.button('Con mèo')
with col2: 
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con đại bàng')
with col4: 
    b4 = st.button('Con khỉ')
with col5:
    b5 = st.button('Con kiến')
with col6: 
    b6 = st.button('Con thỏ')

if b1:
    with subCol1:
        st.write("Âm thanh")
        audio = open("tieng_meo_keu-www_tiengdong_com.mp3",'rb')
        st.audio(audio,format="audio/wav")

        st.write("Video")
        video="https://www.youtube.com/watch?v=tBpOdJ_G-sQ"
        st.video(video,format="mp4/video")
    with subCol2:
        img = 'https://th.bing.com/th/id/R.df2595e64b427e542ee04a1b979065b9?rik=wgTN9eXyNSLPzw&pid=ImgRaw&r=0'
        st.image(img,caption='Con đại bàng')
