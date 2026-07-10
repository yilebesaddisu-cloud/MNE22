import streamlit as st
import time as T
st.image ("OAF.jpg")
#title
st.title ("Welcome to OAF")

#header
st.header ("Baseline Survey Status")

#sub-header
st.subheader ("Farmers Survey")

st.info ("Information Details of the survey")

st.warning ("Come on time otherwise you will be marked as absent")

st.write ("Enumerator Name")
st.write ("range (50)")
st.write (range (50))

st.warning ("xxxx")
st.success ("congra")

st.markdown ("# OAF")
st.markdown ("## OAF")
st.markdown ("### OAF")

st.markdown (":moon:")
st.markdown (":sunglass:")
st.text ("Enumerators Performance")
st.caption ("Caption")
#to enter mathematical formula
st.latex (r'''a+b X^2+c''')

#widget
#checkbox
st.checkbox ('login')
#button
st.button ("click")
#radio widget
st.radio ("Pick Your Gender",["Male","Female","Other"])
#select box
st.selectbox ("select your favorite seedling", ["Gravillea", "Gesho", "Mango", "Papaya"])
#multiselect
st.multiselect("select the seedlings you have taken in 2026", ["Gravillea", "Gesho", "Mango", "Papaya"])
#select slider
st.select_slider ("Rating", ["Bad","Good","Excellent","Outstanding"])
#slider
st.slider ("enter your number", 0,100)
#number_input
st.number_input ("Pick your number",0,100)
#text_input
st.text_input ("Enter Your Email Adress")
#date_input
st.date_input ("Data collection date")
#time_input
st.time_input ("What is the time?")
#text_area
st.text_area ("What is your comment on OAF services?")
#file_upload
st.file_uploader ("Upload your CV")
#color
st.color_picker ("color")
#progress
st.progress (90)
#spinner
with st.spinner("Just wait"):
    T.sleep (2)
#ballon
st.balloons()

#sidebar
st.sidebar.title ("Welcome to OAF Services")
st.sidebar.text ("Farmers First")
st.sidebar.text_input ("Email")
st.sidebar.text_input ("Password")
st.sidebar.button ("Submit")
st.sidebar.radio ("Professional Expert", ["Enumerator", "Admin"])

#Data Visualization
import pandas as pd
import numpy as np
st.title ("Bar Chart")
data= pd.DataFrame (np.random.randn (50,2), columns=["X","Y"])
st.bar_chart (data)
st.title ("Line chart")
st.line_chart(data)
st.title ("Area chart")
st.area_chart(data)
st.write ("Thank You!!")









