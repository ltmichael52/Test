import streamlit as st

image1 = 'images.jpg'
image2 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHTzh9nzKuLlkG1JhRxQAxJQ4xdBQE8y4_lQ&s'

st.image(image1,caption='Cat1')
st.image(image2,caption='Cat2',width=500)
sound = open('Tấm Lòng Cửu Long.mp3','rb') 
#read binary
st.audio(sound,format='audio/mp3')

video = 'https://www.youtube.com/watch?v=xfG1AI4s5l0&t=8s'
st.video(video,format='video/mp4')