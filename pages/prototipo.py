
import streamlit as st 
import pandas as pd 
from actions.predict import predict 

from utils.config import set_config 
from const import FORM_SCHEMA

set_config("Prototipo")

st.header("Prototipo", divider=True)

indicators = {}

with st.form(key='main_form'):
    st.subheader("Formulario")

    for field in FORM_SCHEMA: 
        feat, type, question, tip = field[:4]

        if type == "number":
            value, min_value, max_value, step = field[4]
            
            if feat in ["MentHlth", "PhysHlth"]:
                ans = st.slider(question,min_value, max_value, value, step,help=tip)
            else:
                ans = st.number_input(question,min_value, max_value, value, step,help=tip)
            
        elif type == "select":
            ans = st.selectbox(question, field[4], help=tip)
        else: # Bin
            ans = st.checkbox(question, value=False, help=tip)
        
        indicators[feat] = ans

    submitted = st.form_submit_button('Enviar', type="primary")

if submitted:

    with st.spinner("Cargando..."):
        try:
            result = predict(indicators)
            
            st.subheader("Resultados")

            if result["prediction"]:
                st.error("Alta probabilidad de sufrir diabetes tipo II. Te recomendamos consultar un especialista para obtener más información.", icon="🚨")                
            else:
                st.success('Baja probabilidad de tener diabetes tipo II.', icon="✅")

            st.subheader("Información adicional")

            st.info(f"BMI {result['BMI']:.2f}: {result['status']}")

            st.link_button("Evaluanos", "/review")
        except:
            st.toast('Ocurrio un error inesperado. Por favor, intente nuevamente.')