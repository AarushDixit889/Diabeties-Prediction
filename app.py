import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.header("Diabeties Prediction")
pregnancies=st.number_input("Pregnancies",min_value=0)
glucose=st.number_input("Glucose",min_value=0)
bloodpressure=st.number_input("Blood Pressure",min_value=0)
skinthickness=st.number_input("Skin Thickness",min_value=0)
insulin=st.number_input("Insulin",min_value=0)
bmi=st.number_input("BMI",min_value=0)
diabetespedigreefunction=st.number_input("Diabetes Pedigree Function")
age=st.number_input("Age",min_value=0)
if st.button("Predict"):
    inp=pd.DataFrame({"pregnancies":pregnancies,"glucose":glucose,"bloodpressure":bloodpressure,"skinthickness":skinthickness,"insulin":insulin,"bmi":bmi,"diabetespedigreefunction":diabetespedigreefunction,"age":age},index=pd.RangeIndex(0,500))
    model=pickle.load(open("pipe.pkl","rb"))
    prediction=model.predict(inp)[0]
    if prediction==[0]:
        prediction="No,You don't have problem of diabeties"
    else:
        prediction="Yes,You have problem of diabeties"
    st.text(prediction)