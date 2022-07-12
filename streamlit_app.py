import streamlit as st
import subprocess
from PIL import Image

st.header('🎈 App Name')


st.subheader('Printing text in R')

process1 = subprocess.Popen(["Rscript", "helloworld.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)


st.subheader('Creating a plot using ggplot2')

code2 = '''library(ggplot2)

ggplot(mtcars, aes(mpg, wt)) +
  geom_point()

ggsave('plot.png')
'''
st.code(code2, language='R')

process2 = subprocess.Popen(["Rscript", "plot.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process2.communicate()
image = Image.open('plot.png')
st.image(image)
