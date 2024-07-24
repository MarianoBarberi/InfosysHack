# python -m run streamlitapp.py

import streamlit as st
from dashboard import dash
from tryInput import ask

# Set page config
st.set_page_config(page_title="JUMBAI", page_icon=':computer:', layout="wide")


# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Ask", "Dashboard", "+"])

if page == "Dashboard":
    dash()
elif page == "Ask":
    ask()
elif page == "+":
    st.title("+")
    st.write("GAN model to generate synthetic transaction data for fraud detection.")
    st.write("GAN model will generate one class of data (non-fraudulent transactions) and the discriminator will learn to distinguish between real and fake data.")