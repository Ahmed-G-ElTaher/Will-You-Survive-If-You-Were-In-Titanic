import streamlit as st
import numpy as np
import pandas as pd
from joblib import load 


st.set_page_config(
    page_title='Will You Survive If You Were In Titanic ? :ship:',
    layout='centered',
    initial_sidebar_state='expanded'
)


data= pd.read_csv('Taitanic.csv') 


st.sidebar.image('https://i.pinimg.com/564x/8a/5d/95/8a5d9586fbe7a3cbd0dad8c9c160e898.jpg')
st.image('https://www.financialexpress.com/wp-content/uploads/2023/06/Sub-Cover.jpg?w=580')
st.title('Will You Survive If You Were In Titanic ? :ship:')

'''
    [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Ahmed-G-ElTaher/Churn-Model-on-Data-Science-and-Analytics-Virtual-Intern-at-BCG)
'''
st.markdown("<br>",unsafe_allow_html=True)
'''
    [![Account](https://camo.githubusercontent.com/571384769c09e0c66b45e39b5be70f68f552db3e2b2311bc2064f0d4a9f5983b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476d61696c2d4431343833363f7374796c653d666f722d7468652d6261646765266c6f676f3d676d61696c266c6f676f436f6c6f723d7768697465)](mailto:ahmed.g.eltaher@gmail.com) 
    [![Account](https://camo.githubusercontent.com/a80d00f23720d0bc9f55481cfcd77ab79e141606829cf16ec43f8cacc7741e46/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d3030373742353f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/ahmed-el-taher/) 
'''

st.markdown("<br>",unsafe_allow_html=True)
'---------------------------------------------'
st.header("Input Your Data ")
st.header("To Know If You Lucky To Survive ")

'---------------------------------------------'



model = load('cat.joblib')


columns = ['Sex','Age','Pclass','Fare','Embarked','SibSp','Parch']

name  = st.text_input("Input Your Name : ", 'John Smith')
Sex0 = st.selectbox("Choose Your Gender : ", ['male','female'])
if Sex0 == 'male' :
    Sex = 1
elif Sex0 == 'female' :
    Sex = 0
Age = st.slider("Choose Your Age : ",0,100)
SibSp = st.slider("How Many Siblings Will You Take With You ? ",0,8)
Parch = st.slider("Will You Take One Of Your Parents Or Not ? ",0,2)
Embarked = st.selectbox("Choose Your Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)", ['S','C','Q'])

Fare = st.number_input("Input Fare Price You Will Pay To Book A Ticket : ", 0,520)

if Fare :
    id = data[data['Fare'] >= Fare]['PassengerId'].sample(n=1).values[0]
    passengerid = st.write("Your ID Passenger Is: ", id) 

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

    booking = data[data['Fare'] >= Fare]['Ticket'].sample(n=1).values[0]
    ticket = st.write("Your Ticket Number Is: ", booking) 


    room = data[data['Fare'] >= Fare]['Cabin'].dropna().sample(n=1).values[0]
    cabin = st.write("Your Cabin Is: ", room)

    if Embarked == 'C' :
        Embarked = 0
    elif Embarked == 'S' :
        Embarked = 2
    else :
        Embarked = 1

    

    trigger = st.button('Predict Your Fate',use_container_width=True,type='primary')

    if trigger :
        row = np.array([Sex,Age,Pclass,Fare,Embarked,SibSp,Parch]) 
        X = pd.DataFrame([row], columns = columns)
        prediction = model.predict(X)
        if prediction[0] == 1: 
                st.write('Passenger Survived :thumbsup:')
                with st.expander("Your Fate",expanded=True):
                    st.write("Don't worry you are in survive boat.")
                    st.image("https://cdn.arstechnica.net/wp-content/uploads/2023/02/jack5.jpg")
        else: 
            st.write('Passenger did not Survive :thumbsdown:')
            if Sex0 == 'male' :
                with st.expander("Your Fate",expanded=True):
                        st.write("unfortunately, you didn't Survive.")
                        st.image("https://thumbs.gfycat.com/DifficultNimbleAntbear-size_restricted.gif")
            else :
                with st.expander("Your Fate",expanded=True):
                        st.write("unfortunately, you didn't Survive.")
                        st.image("https://s3.amazonaws.com/snwceomedia/ame-egl/ebb15fca-2426-412c-b7f2-dba39077efb2.sized-1000x1000.gif?w=1000")