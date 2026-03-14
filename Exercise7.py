import streamlit as st

st.set_page_config(page_title='Trắc nghiệm tính cách',page_icon=':question:',layout='wide')
st.title('Hãy chọn một con vật yêu thích')

Persionality = {'Con chó': 'Thân thiện, hoạt boát' , 
                'Con mèo': 'Dịu dàng', 
                'Con sư tử': 'Mạnh mẽ',
                'Con ngựa':'Nhanh nhẹn', 
                'Thiên nga':'Tốt bụng'
}

col1 , col2, col3, col4,col5= st.columns(5)
with col1:
    b1 = st.button('Con mèo')
with col2: 
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con ngựa')
with col4: 
    b4 = st.button('Con sư tử')
with col5:
    b5= st.button('Thiên nga')

if b1:
    with st.expander('Con mèo'):
        st.write(Persionality['Con mèo'])
if b2:
    with st.expander('Con chó'):
        st.write(Persionality['Con chó'])
if b3:
    with st.expander('Con ngựa'):
        st.write(Persionality['Con ngựa'])
if b4:
    with st.expander('Con sư tử'):
        st.write(Persionality['Con sư tử'])
if b5:
    with st.expander('Thiên nga'):
        st.write(Persionality['Thiên nga'])

with st.sidebar:
    st.title('Trắc nghiệm tính cách')
    if b1:
        st.write('Con vật bạn chọn là con mèo')
    if b2:
        st.write('Con vật bạn chọn là con chó')
    if b3:
        st.write('Con vật bạn chọn là con ngựa')
    if b4:
        st.write('Con vật bạn chọn là con sư tử')
    if b5:
        st.write('Con vật bạn chọn là thiên nga')
