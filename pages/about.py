import streamlit as st 

from utils.config import set_config 

set_config("Sobre nosotros")

st.header("Sobre nosotros", divider=True)

cols = st.columns(3)


with cols[0]:
    st.image("assets\img\sonya-wins.jpg")
    st.write("**Sonya Castro**")
    st.write("""
        Ingeniería de Sistemas
        Universidad del Norte
        Barranquilla, Colombia
    """)
    st.write("sonyac@uninorte.edu.co")
    st.link_button(
        "Ver Linkedin",
        "https://www.linkedin.com/in/sonya-castro/",
        type="secondary",
        use_container_width=True
    )
    
with cols[1]:
    st.image("assets\img\señorito refri.png")
    st.write("**Fifi Felix**")
    st.write("""
        Ingeniería de Sistemas
        Universidad del Norte
        Barranquilla, Colombia
    """)
    st.write("felixj@uninorte.edu.co")
    st.link_button(
        "Ver Linkedin",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        type="secondary",
        use_container_width=True
    )

with cols[2]:
    st.image("assets\img\dario.jpg")
    st.write("**Mario Valencia**")
    st.write("""
        Ingeniería de Sistemas
        Universidad del Norte
        Barranquilla, Colombia
    """)
    st.write("jdario@uninorte.edu.co")
    st.link_button(
        "Ver Linkedin",
        "https://www.linkedin.com/in/dario-mejia/",
        type="secondary",
        use_container_width=True
    )

st.subheader("Nuestro tutores")
cols = st.columns(2)

with cols[0]:
    st.write("**Eduardo Angulo**")
    st.write("""
        Ingeniería de Sistemas
        Universidad del Norte
        Barranquilla, Colombia
    """)
    st.write("edangulo@uninorte.edu.co")
    
with cols[1]:
    st.write("**Wilson Nieto**")
    st.write("""
        Ingeniería de Sistemas
        Universidad del Norte
        Barranquilla, Colombia
    """)
    st.write("wnieto@uninorte.edu.co")

