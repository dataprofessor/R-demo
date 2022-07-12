import streamlit as st
import subprocess
from PIL import Image

st.header('🎈 App Name')

st.write('Hello world!')

process1 = subprocess.Popen(["echo", "Hello, World!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process1.communicate()
st.write(result2)

process2 = subprocess.Popen(["Rscript", "helloworld.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process2.communicate()
st.write(result2)

process = subprocess.Popen(["Rscript", "plot.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result3 = process.communicate()
image = Image.open('plot.png')
st.image(image)
