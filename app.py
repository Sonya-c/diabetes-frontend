import streamlit as st 
import pandas as pd 
import streamlit_shadcn_ui as ui

from utils.config import set_config 
import const as content

@st.cache_data(show_spinner=False)
def get_file(path):
    with open(path, "rb") as f:
        return f.read()

set_config("Home")

st.image("assets/img/banner.png", use_column_width=True)
st.header(content.TITLE)

cols = st.columns(5)
with cols[0]:
    st.write("**Sonya Castro**")

with cols[1]:
    st.write("**Jeffrey Felix**")

with cols[2]:
    st.write("**Dario Mejia**")

with cols[3]:
    st.write("**Eduardo Angulo**")

with cols[4]:
    st.write("**Wilson Nieto**")


with ui.card("Resumen"):
    # st.subheader("Abstract")
    ui.element("p", children=[content.ABSTRACT])

st.download_button(
    'Descargar informe completo',
    data=get_file("./assets/report.pdf"),
    file_name="report.pdf",
    mime='application/octet-stream'
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Introducción")
    st.write(content.INTRODUCCION)
    
    st.subheader("Problema")

    st.subheader("Justificación")
    st.write(content.JUSTIFICACION)

    st.subheader("Objetivos")
    st.write(content.OBJECTIVOS)

    st.subheader("Metodología")
    st.image(
        "assets/crips_ml.png",
        caption="CRIPS-ML(Q) | Imagen por Abid Ali Awan"
    )

    st.subheader("Aspectos Teóricos")
    st.write(content.ASPECTOS_TEORICOS)

with col2:
    st.subheader("Diseño solución (arquitectura)")
    st.image(
        "assets/img/arch.png",
        caption="Arquitectura de despliegue"
    )

    st.subheader("Prototipo")
    st.link_button(
        "Ir a prototipo",
        "/prototipo"
    )

    st.subheader("Resultados")
    st.write(content.RESULTADOS)
    st.image("assets/img/cm_rf.png")
    st.image("assets/img/cm_esemble.png")
    df = pd.DataFrame(content.RESULTADOS_TABLA)
    df = df.set_index('modelo')
    st.data_editor(df)

    
st.subheader("Conclusiones")
st.write(content.CONCLUSIONES)







