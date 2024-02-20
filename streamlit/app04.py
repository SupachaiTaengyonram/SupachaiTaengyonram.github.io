import streamlit as st
from diffusers import DiffusionPipeline as dp
from PTL import Image
h = st.header('My web site')
p = st.write('Im Datascince Sortware')
s = st.subheader('WHO AM I')
banner = st.image('https://png.pngtree.com/thumb_back/fh260/background/20230612/pngtree-the-anime-anime-girl-in-autumn-leaves-wearing-a-long-red-image_2957988.jpg')
b = st.button('click me')
text = st.text_input('Promt :')
if text:
    dp = DP.from_pretrained('runwayml/stable-diffusion-v1-5),
                            torch_dtupe=torch.float16)
    
    st.image('https://picsum.photos/400/200')
    b = st.button('To continue...')