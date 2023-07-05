import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import joblib

st.set_page_config(
    page_title='Will You Survive If You Were In Titanic ? :ship:',
    layout='centered',
    initial_sidebar_state='expanded'
)

st.sidebar.image('https://i.pinimg.com/564x/8a/5d/95/8a5d9586fbe7a3cbd0dad8c9c160e898.jpg')
st.image('https://hips.hearstapps.com/hmg-prod/images/the-white-star-line-passenger-liner-r-m-s-titanic-embarking-news-photo-1608252641.?crop=1xw:0.75xh;center,top&resize=1200:*')
st.title('Will You Survive If You Were In Titanic ? :ship:')

'''
    [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Ahmed-G-ElTaher/Churn-Model-on-Data-Science-and-Analytics-Virtual-Intern-at-BCG)
'''
st.markdown("<br>",unsafe_allow_html=True)
'''
    [![Account](https://camo.githubusercontent.com/571384769c09e0c66b45e39b5be70f68f552db3e2b2311bc2064f0d4a9f5983b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476d61696c2d4431343833363f7374796c653d666f722d7468652d6261646765266c6f676f3d676d61696c266c6f676f436f6c6f723d7768697465)](mailto:ahmed.g.eltaher@gmail.com) 
    [![Account](https://camo.githubusercontent.com/a80d00f23720d0bc9f55481cfcd77ab79e141606829cf16ec43f8cacc7741e46/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d3030373742353f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/ahmed-el-taher/) 
'''

'''
   

'''
st.markdown("<br>",unsafe_allow_html=True)
'---------------------------------------------'
st.header("Input Your Data ")
st.header("To Know If You Lucky To Survive ")

'---------------------------------------------'



model = joblib.load('cat.joblib')


columns = ['Sex','Age','Pclass','Fare','Embarked','SibSp','Parch']

name  = st.text_input("Input Passenger Name", 'John Smith')
Sex = st.selectbox("Choose sex", ['male','female'])
if Sex == 'male' :
    Sex = 1
elif Sex == 'female' :
    Sex = 0
Age = st.slider("Choose age",0,100)
SibSp = st.slider("Choose siblings",0,8)
Parch = st.slider("Choose parch",0,2)
Embarked = st.selectbox("Did they Embark?", ['S','C','Q'])
Fare = st.number_input("Input Fare Price", 0,520)


passengerid = st.write("Your ID Passenger Is: ") 
ticket = st.text_input("Input Ticket Number", "12345") 
c = 0
if Fare <= 150 :
    c = 'Third Class'
    C=3
elif 150 < Fare < 350 :
    c = 'Second Class'
    C=2
elif Fare >= 350 :
    c = 'First class'
    C=1 
Pclass = st.write("Your Class Is: " , c )

cabin = st.text_input("Input Cabin", "C52") 

if Embarked == 'C' :
    Embarked = 0
elif Embarked == 'S' :
    Embarked = 2
else :
    Embarked = 1

def predict(): 
    row = np.array([Sex,Age,Pclass,Fare,Embarked,SibSp,Parch]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success('Passenger Survived :thumbsup:')
    else: 
        st.error('Passenger did not Survive :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)


