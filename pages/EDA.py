import streamlit as st 

from actions.eda_actions import get_data, yassify_data
from utils.config import set_config 
from widgets.eda_widgets import pie_plot, bar_chart, corr, corr_bars, dist, outliner_plot

set_config("EDA")

st.header("Análisis exploratorio de datos", divider=True)
df = get_data()
df_yass = yassify_data(df)

st.subheader("Variable objetivo")
pie_plot(df_yass)

st.subheader("Variables binarias")
bin_vars = ['HighBP', 'HighChol', 'CholCheck','Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk']

selected_bin_var = st.selectbox("Seleccione una variable", bin_vars)
bar_chart(df_yass, selected_bin_var)

st.subheader("Corelaciones")
corr(df)
corr_bars(df)

st.subheader("Distribuciones")
vars = ["GenHlth", "HighBP", "DiffWalk", "BMI", "HighChol", "Age", "HeartDiseaseorAttack", "PhysHlth", "Education", "Income"]
selected_col_dist = st.selectbox("Seleccione una variable", vars)

st_cols = st.columns(2)
dist(df, selected_col_dist)

st.subheader("Datos atípicos")
vars = ['BMI', 'GenHlth', 'MentHlth', 'PhysHlth', 'Age','Education', 'Income']
selected_col_outliner = st.selectbox("Seleccione una variable", vars)
outliner_plot(df, selected_col_outliner)