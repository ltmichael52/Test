import streamlit as st

with st.sidebar:
    image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYW_ro7UCV1oihiq9Krh7YCwcM0qyFYQH_cg&s'
    st.image(image,caption='Den Vau')
    st.write('Họ và tên: Nguyễn Đức Cường')
    st.write('Nghệ Danh: Đen Vâu')
    st.write('Là ca sĩ nam được yêu thích nhất việt nam')

st.title('Bài hát yêu thích')
st.write('Gieo Quẻ')

audio = open('Gieo Quẻ.mp3','rb')
st.audio(audio,format= 'audio/mp3')

st.title('MV yêu thích')
st.write('Vị nhà')

video='https://www.youtube.com/watch?v=Hqmbo0ROBQw'
st.video(video,format='video/mp4')

