import streamlit as st 

st.title("Welcome to BMI calculator")

st.write("Enter your weight in (kg)")
weight =float ( st.number_input("Enter your weight in kg"))

st.write("Enter your height in (m)")
height =float (st.number_input("Enter your height in m"))

st.button("Calculate BMI")

if height == 0:
    st.write("height cannot be zero")
else:
    bmi=float(weight/(height**2))
    st.write(f"Your BMI is {bmi}")
    if (bmi < 18.5):
       st.success("Your bmi is underweight")
    
    elif (18.5 <= bmi < 24.9):
       st.success("Your bmi is normal")
    
    elif (24.9 <= bmi < 29.9):
       st.write("Your bmi is overweight")
    else:
       st.error("error")
    



