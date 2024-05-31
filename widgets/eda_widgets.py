import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from actions.eda_actions import create_plot_pivot

sns.set_palette("Set2")
palette = sns.color_palette()

def pie_plot(df):
    labels=["No diabetico","Diabetico"]
    
    fig, ax = plt.subplots(figsize=(20,5))
    ax.pie(
        df["Diabetes_binary"].value_counts(), 
        labels =labels,
        autopct='%.02f',
    )
    st.pyplot(fig)

def bar_chart(df, col):
    fig, ax = plt.subplots(figsize=(10,5))
    df_pivoted = create_plot_pivot(df, col).plot(kind='bar',stacked=True, ax=ax)
    st.pyplot(fig)

def corr(df):
    plt.figure(figsize = (20,10))
    plt.title("Correlación de Features")
    plot = sns.heatmap(df.corr(),annot=True , cmap ='YlGnBu')
    st.pyplot(plot.get_figure())


def corr_bars(df):
    fig, ax = plt.subplots()
    (df.drop('Diabetes_binary', axis=1)
    .corrwith(df.Diabetes_binary)
    .sort_values(ascending=False)
    .plot(kind='bar', figsize=(12, 4), title="Corelación Diabetes_binary", alpha=0.8, zorder=3, ax=ax)
    .spines[['top','right', 'left']].set_visible(False)
    )
    plt.grid(axis='y', linestyle='--', alpha=.5)
    plt.xticks(rotation = 45, ha='right', size=15)
    st.pyplot(fig)

def dist(df, col):
    labels = {
        "GenHlth": ['Excelente', 'Muy buena', 'Buena', 'Mala', 'Pobre'],
        "HighBP": ["No", 'Si'],
        "DiffWalk": ["No", 'Si'],
        "BMI_bins": ['Bajo peso', 'Peso saludable', 'Sobrepeso', 'Obesidad'],
        "HighChol": ["No", 'Si'],
        "Age": ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+'],
        "HeartDiseaseorAttack": ["No", 'Si'],
        "Education": ["Nunca asistió a la escuela o solo al jardín de infantes", "Grados 1 a 8 (Primaria)", "Grados 9 a 11 (Algunas escuelas secundarias)", "Grado 12 o GED (Graduado de escuela secundaria)", "Universidad 1 año a 3 años (Alguna universidad o escuela técnica)", "Universidad 4 años o más (Graduado universitario)"],
        "Income": ['<10,000', '10,000-15,000', '15,000-20,000', '20,000-25,000', '25,000-35,000', '35,000-50,000', '50,001-75,000', '>75,000']
    }

    if col == "BMI":
        bins = [0, 18.5, 24.9, 29.9, float('inf')]
        bin_labels = [1,2,3,4]
        df['BMI_bins'] = pd.cut(df['BMI'], bins=bins, labels=bin_labels)
        col = "BMI_bins"

    ratio = 3
    fig, (ax, ax2) = plt.subplots(1,2, figsize=(ratio*3.2,ratio), dpi=200, sharey=True)
    fig.suptitle(f'Distribución de {col}')

    (df[df['Diabetes_binary']==False][col]
    .value_counts(1)
    .sort_index()
    .plot(ax=ax,kind='bar', zorder=3, color=palette)).spines[['top','right', 'left']].set_visible(False)
    ax.set_xlabel('Sin Diabetes',size=8)

    if labels.get(col, None) != None and col != "Education":
        ax.set_xticklabels(labels.get(col))

    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    ax.grid(axis='y', linestyle='--', alpha=.5)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

    (df[df['Diabetes_binary']==True][col]
    .value_counts(1)
    .sort_index()
    .plot(ax=ax2, kind='bar', zorder=3, color=palette)).spines[['top','right', 'left']].set_visible(False)
    ax2.set_xlabel('Con Diabetes',size=8)
    if labels.get(col, None) != None and col != "Education":
        ax2.set_xticklabels(labels.get(col))

    ax2.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    ax2.grid(axis='y', linestyle='--', alpha=.5)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

    st.pyplot(fig)

    if col == "Education":
        for i, label in enumerate(labels[col]):
            st.write(f"{i + 1}. {label}")    

def outliner_plot(df, col):
    fig, ax = plt.subplots(figsize=(5, 3))

    sns.boxplot(x = col, data = df, palette='Set2')
    st.pyplot(fig)
