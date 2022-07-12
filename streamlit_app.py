import streamlit as st
import subprocess
from PIL import Image

st.header('🎈 App Name')

st.write('Hello world!')

process = subprocess.Popen(["echo", "Hello, World!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process.communicate()
st.write(result2)


process = subprocess.Popen(["Rscript", "helloworld.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process.communicate()
st.write(result2)

image = Image.open('plot.png')
st.image(image)
