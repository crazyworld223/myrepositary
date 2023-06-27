import streamlit as st 
st.set_page_config(page_title='my cool zone',page_icon='smile')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://nykdaily.com/wp-content/uploads/2020/04/maxresdefault-2.jpg')
st.title('My Crazy World')
st.header('By Akash Pathak')
st.text('This is my first page by using streamlit')
if (mymenu=='Home'):
    st.markdown('<center><h1>Hii guys do you remember POPAAYE :) </h1></center>',unsafe_allow_html=True )
    st.video('https://www.youtube.com/watch?v=PFulYCqdXnQ')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        ratings=st.slider('Choose Ratings')
        k=st.form_submit_button('Submit Form')
elif(mymenu=='Downloads'):
    st.header('Downloads')
    st.download_button('Download Now','Awww Thanks for visiting my page ')