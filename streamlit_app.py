import streamlit as st
import subprocess

st.header('🎈 App Name')

st.write('Hello world!')

process = subprocess.Popen(["echo", "Hello, World!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process.communicate()
st.write(result2)


process = subprocess.Popen(["R CMD BATCH", "helloworld.r"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process.communicate()
st.write(result2)
