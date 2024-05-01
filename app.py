import streamlit as st 

with open("./assets/report.pdf", "rb") as pdf_file:
    report = pdf_file.read()

st.title("Diseño e Implementaión de una Aplicación para el Diagnostico y Detecciónn Temprana de Diabetes Tipo 2")
st.write("Sonya Castro; Jeffrey Felix; Dario Mejia; Wilson Nieto; Eduardo Angulo.")

st.download_button(
    'Download PDF',
    data=report,
    file_name="report.pdf",
    mime='application/octet-stream'
)

st.divider()

st.subheader("Abstract")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi congue porta dapibus. Etiam auctor dolor ut purus consectetur sagittis. Proin mollis eleifend ex, non luctus ex maximus quis. Sed ornare felis eget nulla elementum, vel blandit neque pellentesque. Mauris dictum dui in eros fermentum sodales. Aliquam sodales pulvinar urna non gravida. Quisque dapibus luctus neque, quis aliquet elit dapibus non. Morbi nec velit elit. Nulla euismod consectetur libero, quis congue eros sodales nec. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed sed elementum odio. Mauris tincidunt lectus nec auctor tristique. Nunc et commodo lectus, a finibus erat.")