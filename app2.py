import streamlit as st

st.title("kindly add city and age")
age = st.slider("Select your age:", 1,100)
city = st.selectbox("Select your city:", ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])

if st.button("Submit"):
    st.write("age:", age)
    st.write("city:", city)