import streamlit as st

h = st.header('My web site')
p = st.write('Im Datascince Sortware')
s = st.subheader('WHO AM I')
banner = st.image('https://png.pngtree.com/thumb_back/fh260/background/20230612/pngtree-the-anime-anime-girl-in-autumn-leaves-wearing-a-long-red-image_2957988.jpg')
b = st.button('click me')
text = st.text_input('Promt :')
if text:
    st.image('https://picsum.photos/400/200')
    b = st.button('To continue...')