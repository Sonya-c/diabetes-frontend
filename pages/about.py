import streamlit as st 

from utils.config import set_config 

set_config("Sobre nosotros")

st.header("Sobre nosotros", divider=True)

cols = st.columns(3)


with cols[0]:
    st.image("assets/img/sonya-wins.png")
    st.write("**Sonya Castro**")
    st.markdown("""
        <p>
            Ingeniería de Sistemas</br>
            Universidad del Norte</br>
            Barranquilla, Colombia
        </p>
    """, unsafe_allow_html=True)
    st.write("sonyac@uninorte.edu.co")
    st.link_button(
        "Ver Linkedin",
        "https://www.linkedin.com/in/sonya-castro/",
        type="secondary",
        use_container_width=True
    )
    
with cols[1]:
    st.image("assets/img/señorito fifi.png")
    st.write("**Jeffrey Felix**")
    st.markdown("""
        <p>
            Ingeniería de Sistemas</br>
            Universidad del Norte</br>
            Barranquilla, Colombia
        </p>
    """, unsafe_allow_html=True)
    st.write("felixj@uninorte.edu.co")
    st.link_button(
        "Ver Linkedin",
        "https://www.linkedin.com/in/jeffrey-felix-b45519302/",
        type="secondary",
        use_container_width=True
    )

with cols[2]:
    st.image("assets/img/Mario.png")
    st.write("**Dario Mejia**")
    st.markdown("""
        <p>
            Ingeniería de Sistemas</br>
            Universidad del Norte</br>
            Barranquilla, Colombia
        </p>
    """, unsafe_allow_html=True)
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
    st.markdown("""
        <p>
            Ingeniería de Sistemas</br>
            Universidad del Norte</br>
            Barranquilla, Colombia
        </p>
    """, unsafe_allow_html=True)
    st.write("edangulo@uninorte.edu.co")
    
with cols[1]:
    st.write("**Wilson Nieto**")
    st.markdown("""
        <p>
            Ingeniería de Sistemas</br>
            Universidad del Norte</br>
            Barranquilla, Colombia
        </p>
    """, unsafe_allow_html=True)

    st.write("wnieto@uninorte.edu.co")

