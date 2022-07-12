import streamlit as st
import subprocess

st.header('🎈 App Name')

st.write('Hello world!')

result1 = subprocess.run(["echo", "Hello, World!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
st.write(result1.stdout)

result2 = subprocess.run(["R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
st.write(result2.stdout)
