import streamlit as st

st.set_page_config(page_title='Bài 7',page_icon=':smile:',layout='wide',initial_sidebar_state='collapsed')
st.title('Hello')
st.write('Lập trình trang web')

with st.expander('Số nguyên'):
    st.write('5')
    st.write('3')
    st.write('7')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('A Cat')
    st.write('Mèo thích ăn pa tê')
with col2: 
    st.header('A Dog')
    st.write('Chó thích ăn xương')
with col3:
    st.header('A Rabbit')
    st.write('Thỏ thích ăn cỏ')

st.sidebar.write('1.Lời nói đầu')
with st.sidebar:
    st.write('2.Mục lục')