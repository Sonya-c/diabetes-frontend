
import streamlit as st 
import pandas as pd 
from actions.predict import predict 

st.header("Prototipo", divider=True)

indicators = {}

FORM = [    
    # Para el calculo del BMI
    ("height", "number", "Altura (metros)", None, (1.6, 1.0, None, 0.1)),
    ("weight", "number", "Peso (kg)", None, (50.0, 1.0, None, 0.1)),    
    ("Sex", "select", "Sexo", None, ("M", "F")),
    ("Age", "number", "Edad", None, (18, 1, None, 1)),
    ("Income", "number", "Ingreso (dolares)", None, (0.0, 0.0, None, 100.0)),
    ("Education", "select", "Educación", None, ["Nunca/Solo jardin", "Primaria", "Bachillerato (parcial)", "Bachillerato (graduado)", "Universidad/Tecnico (parcial)", "Universidad/Tecnico (graduado)"]),

    # ¿Bebedores empedernidos? (hombres adultos que toman mas de 14 tragos por semana y mujeres adultas que toman mas de 7 tragos por semana)
    ("AlcoholConsump", "number", "¿Cúantos tragos bebe por semana?", None, (0, 0, None, 1)),

    ("HighBP", "bin", "¿Tiene presion arterial alta?", None),
    ("HighChol", "bin", "¿Tiene colesterol alto?", None),
    ("CholCheck", "bin", "¿Se ha realizado un chequeo de colesterol en 5 años?", None),
    ("Smoker", "bin", "¿Ha fumado al menos 100 cigarros en su vida entera?", None),
    ("Stroke", "bin", "¿(Alguna vez le dijeron) que tuvo un derrame cerebral?", None),
    ("HeartDiseaseorAttack", "bin", "¿Tiene enfermedad coronaria o infarto de miocardio?", None),
    ("PhysActivityFeature", "bin", "¿Ha realizado actividad física en los ultimos 30 días? (Sin incluir el trabajo)", None),
    ("Fruits", "bin", "¿Consume fruta 1 o más veces al día?", None),
    ("Veggies", "bin", "¿Consume verduras 1 o más veces al día?", None),
    ("AnyHealthcare", "bin", "¿Tiene algun tipo de cobertura de atención médica?", "Incluidos seguros medicos, planes prepagos, etc."),
    ("NoDocbcCost", "bin", "¿Hubo algun momento en los últimos 12 meses en el que necesito consultar a un medico pero no pudo debido al costo?", None),
    ("DiffWalk", "bin", "¿Tiene serias dificultades para caminar o subir escaleras?", None),

    ("GenHlth", "select", "¿Cómo diría que es su salud en general?", None, ["Excelente", "Muy buena", "Buena", "Regular", "Mala"]),

    ("MentHlth", "number", "¿Por cúantos de los últimos 30 días su salud mental no fue buena?", "Incluye estrés, depresión y problemas con las emociones", (0, 0, 30, 1)),
    ("PhysHlth", "number", "¿Por cúantos de los últimos 30 días su salud fisica no fue buena?", "Incluye enfermedades físicas y lesiones", (0, 0, 30, 1))

]


with st.form(key='main_form'):
    st.subheader("Formulario")

    for field in FORM: 
        feat, type, question, tip = field[:4]

        if type == "number":
            value, min_value, max_value, step = field[4]
            ans = st.number_input(question,min_value, max_value, value, step,help=tip)
        elif type == "select":
            ans = st.selectbox(question, field[4], help=tip)
        else: # Bin
            ans = st.checkbox(question, value=False, help=tip)
        
        indicators[feat] = ans

    submitted = st.form_submit_button('Enviar')

if submitted:

    with st.spinner("Cargando..."):
        result = predict(indicators)
        
        st.subheader("Resultados")

        if result["prediction"]:
            st.success('Onda vital', icon="✅")
        else:
            st.error("Tienes cancer, Andy", icon="🚨")

        st.subheader("Información adicional")

        st.info(f"BMI {result['BMI']:.2f}: {result['status']}")