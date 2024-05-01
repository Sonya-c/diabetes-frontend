
import streamlit as st 
import pandas as pd 
from actions.predict import predict 

st.header("Prototipo", divider=True)

FORM = [
    ("HighBP", "¿Tiene presion arterial alta?", "bin"),
    ("HighChol", "¿Tiene colesterol alto?", "bin"),
    ("CholCheck", "¿Se ha realizado un chequeo de colesterol en 5 años?", "bin"),
    ("Smoker", "¿Ha fumado al menos 100 cigarros en su vida entera?", "bin"),
    ("Stroke", "¿(Alguna vez le dijeron) que tuvo un derrame cerebral?", "bin"),
    ("HeartDiseaseorAttack", "¿Tiene enfermedad coronaria o infarto de miocardio?", "bin"),
    ("PhysActivityFeature", "¿Ha realizado actividad física en los ultimos 30 días? (Sin incluir el trabajo)", "bin"),
    ("Fruits", "¿Consume fruta 1 o más veces al día?", "bin"),
    ("Veggies", "¿Consume verduras 1 o más veces al día?", "bin"),
    ("BMI", "Índice de masa corporal", "int", 1, 10),
]

indicators = {}

with st.form(key='main_form'):
    for field in FORM: 
        feat, question, type = field[:3]

        if type == "int":
            min_value, max_value = field[3:]
            ans = st.number_input(question, min_value, max_value)
        else: # Bin
            ans = st.checkbox(question, value=False)
        
        indicators[feat] = ans

    submitted = st.form_submit_button('Enviar')

if submitted:
    with st.spinner("Cargando..."):
        res = predict(indicators)
        if res:
            st.success('Onda vital', icon="✅")
        else:
            st.error("Tienes cancer, Andy", icon="🚨")

        st.write(pd.DataFrame.from_dict(indicators, orient='index'))