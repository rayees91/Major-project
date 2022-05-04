import math
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
# st.write(pd.read_excel('dls.xlsx'))
df=pd.read_excel('dls.xlsx')

# df=df.astype("str")
# df["Wickets Lost"]=df["Wickets Lost"].astype(int)
# df["Overs Left"]=df["Overs Left"].astype(int)

# df.head()
# df.head()

choice_fnl = st.sidebar.selectbox("What to Find?",("DLS method", "Average ground score predictor"))


# st.title('DLS Method')
if choice_fnl=="DLS method":
    choice_dls = st.sidebar.selectbox("Select innings ", ("1st Innings", "2nd Innings"))
    def pred1(overstplay,oversplayed,overslost,wicklost,overstplaybyt2,t1s):
        a=(51-(overstplay-oversplayed))
        g50=245
        r1a=df[wicklost][a]*100
        b=a+overslost
        r1b=df[wicklost][b]*100
        # r1=r1a-r1b
        if overslost==0:
            r1=df[0][51-overstplay]*100
        else:
            r1=100-(r1a-r1b)
        r2=df[0][51-(overstplaybyt2)]*100
        if r1>r2:
            t2s=round(t1s*(r2/r1))
        elif r2>r1:
            t2s=round(t1s+g50*(r2-r1)/100)+1
        else:
            t2s=t1s
        return t2s
    def pred2(overstplay,oversplayed,overslost,wicklost,t1s,t2s):
        r1=df[0][51-overstplay]*100
        g50=245
        a=(51-(overstplay-oversplayed))
        r2a=df[wicklost][a]*100
        b=a+overslost
        r2b=df[wicklost][b]*100
        if overslost==0:
            r2=df[0][51-overstplay]*100
        else:
            r2=100-(r2a-r2b)
        if r1>r2:
            rt2s=round(t1s*(r2/r1))
        elif r2>r1:
            rt2s=round(t1s+g50*(r2-r1)/100)+1
        else:
            rt2s=t1s
        st.write("Required runs are:{}".format(rt2s-t2s))
        # st.write(rt2s-t2s)
        return rt2s

    if choice_dls == "1st Innings":
        # df=pd.read_excel('dls.xlsx')
        # df=df.astype("str")
        # st.write(int(df[0][2])*100)
        st.title('DLS Method')
        st.write(round(212*(82.7/95.0)))
        
        # st.write(d.head)
        st.write("Welcome to the Duckworth Lewis Method, this is a mathematical formulation designed to calculate the target score for the team batting second in a limited overs cricket match interrupted by weather or other circumstances.")
        st.write("--------------------------------")
        st.header("If interruption occurs in 1st Innings!")
        overstplay=st.number_input("overs decided to be played at start")
        oversplayed=st.number_input("Number ofovers played")
        overslost=st.number_input("Number of overs lost")
        wicklost=st.number_input("Number of wickets lost")
        overstplaybyt2=st.number_input("Number of overs to be played by team 2")
        t1s=st.number_input("Score at the end of the innings")
        result=""
        if st.button("Find"):
            result=pred1(overstplay,oversplayed,overslost,wicklost,overstplaybyt2,t1s)
        st.success("the par score is {}".format(result))




    elif choice_dls == "2nd Innings":
        st.title('DLS Method')
        st.write("Welcome to the Duckworth Lewis Method")
        st.write("--------------------------------")
        st.header("If interruption occurs in 2nd Innings!")
        overstplay=st.number_input("overs decided to be played at start")
        oversplayed=st.number_input("Number of overs played by t2")
        t2s=st.number_input("Score of Team-2")
        wicklost=st.number_input("Number of wickets lost")
        overslost=st.number_input("Number of overs lost")
        t1s=st.number_input("Runs scored by Team-1")
        result=""
        if st.button("Find"):
            result=pred2(overstplay,oversplayed,overslost,wicklost,t1s,t2s)
        st.success("Revised target is {}".format(result))

    
elif choice_fnl=="Average ground score predictor":
    def pred3(country,groundName,length,width,windSpeed,pitch):
        a=100
        return a
    st.title('Expected Score in New Grounds using Machine Learning')
    country = st.selectbox('In which country match is being played?',
    ('Australia', 'India','England','New Zealand','South Africa','Pakistan',
    'West Indies','Sri Lanka','Afghanistan','Bangladesh','Dubai'))
    groundName = st.text_input('Enter the Ground Name', 'Wankhede Stadium')
    length=st.number_input("Length of the Ground in meters")
    width=st.number_input("Width of the Ground in meters")
    windSpeed=st.number_input("Wind speed in the ground at present")
    pitch = st.selectbox('What is the pitch type?',('Green', 'Dead', 'Dusty'))
    result=""
    if st.button("Find"):
            result=pred3(country,groundName,length,width,windSpeed,pitch)
    st.success("Expected Score in {} is {}".format(groundName,result))
def get_database(classifier_name):
    if classifier_name == "KNN":
        data = datasets.load_iris()
    else:
        data = data
