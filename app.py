
import streamlit as st 

from utils.config import set_config 
from utils.render_pdf import renderPDF

set_config("Home")

st.title("Diseño e Implementaión de una Aplicación para el Diagnostico y Detecciónn Temprana de Diabetes Tipo 2")
st.write("Sonya Castro; Jeffrey Felix; Dario Mejia; Wilson Nieto; Eduardo Angulo.")

st.divider()

# st.download_button(
#     'Download PDF',
#     data=report,
#     file_name="report.pdf",
#     mime='application/octet-stream'
# )

st.subheader("Abstract")
st.write("La diabetes tipo 2 es una enfermedad cronica que representa un desafío significativo para la salud publica mundial, con una prevalencia en aumento y graves riesgos para la salud. En paralelo, el avance tecnologico, especialmente en el campo del Machine Learning (ML), ofrece oportunidades para mejorar el diagnostico y tratamiento de enfermedades. Este estudio propone el desarrollo de un modelo de diagnostico de diabetes tipo 2 basado en ML y Deep Learning (DL), con el objetivo de proporcionar una herramienta precisa y temprana para la deteccion de esta enfermedad. Se utilizarán técnicas avanzadas de ML y DL para aprender de datos pasados y extraer características complejas, con el fin de crear un modelo que pueda ser implementado en una aplicacion web interactiva. Esta aplicación permitira a los usuarios ingresar síntomas relacionados con la diabetes tipo 2 y recibir una evaluacion de riesgo personalizada. Los resultados esperados incluyen un modelo preciso y funcional, así como una aplicacion web accesible que pueda mejorar la deteccion temprana y el tratamiento oportuno de la diabetes tipo 2, contribuyendo así a una atencion médica más efectiva y personalizada.")

renderPDF("./assets/report.pdf")