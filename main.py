import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="📈📈📈📈",
    layout = "wide"

   
)

from PIL import Image
image = Image.open('D:\Azubi LP4\Prediction-Attrition-App\images1.jpg')
st.image(image,use_column_width=False)


st.title("Welcome to our prediction app")
st.text_input("enter your username")
st.text_input("enter your password")
st.button("submit")