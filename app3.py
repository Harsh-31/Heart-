import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("rf.pkl","rb")
rf=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    
    
   
    prediction=rf.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    print(prediction)
    return prediction



def main():
    st.title("Heart Disease Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex","Type Here")
    cp = st.text_input("cp","Type Here")
    trestbps = st.text_input("trestbps","Type Here")
    chol = st.text_input("chol","Type Here")
    fbs = st.text_input("fbs","Type Here")
    restecg = st.text_input("restecg","Type Here")
    thalach = st.text_input("thalach","Type Here")
    exang = st.text_input("exang","Type Here")
    oldpeak = st.text_input("oldpeak","Type Here")
    slope = st.text_input("slope","Type Here")
    ca = st.text_input("ca","Type Here")
    thal = st.text_input("thal","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()