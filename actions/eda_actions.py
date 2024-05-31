import pandas as pd
import streamlit as st 

@st.cache_data(show_spinner="Cargando datos")
def get_data():

    df = pd.read_csv("data/diabetes_binary_health_indicators.csv")
    df["Diabetes_binary"] = df["Diabetes_binary"].astype(int)

    df["HighBP"] = df["HighBP"].astype(int)
    df["HighChol"] = df["HighChol"].astype(int)
    df["CholCheck"] = df["CholCheck"].astype(int)
    df["BMI"] = df["BMI"].astype(int)
    df["Smoker"] = df["Smoker"].astype(int)
    df["Stroke"] = df["Stroke"].astype(int)
    df["HeartDiseaseorAttack"] = df["HeartDiseaseorAttack"].astype(int)
    df["PhysActivity"] = df["PhysActivity"].astype(int)
    df["Fruits"] = df["Fruits"].astype(int)
    df["Veggies"] = df["Veggies"].astype(int)
    df["HvyAlcoholConsump"] = df["HvyAlcoholConsump"].astype(int)
    df["AnyHealthcare"] = df["AnyHealthcare"].astype(int)
    df["NoDocbcCost"] = df["NoDocbcCost"].astype(int)
    df["GenHlth"] = df["GenHlth"].astype(int)
    df["MentHlth"] = df["MentHlth"].astype(int)
    df["PhysHlth"] = df["PhysHlth"].astype(int)
    df["DiffWalk"] = df["DiffWalk"].astype(int)
    df["Sex"] = df["Sex"].astype(int)
    df["Age"] = df["Age"].astype(int)
    df["Education"] = df["Education"].astype(int)
    df["Income"] =df["Income"].astype(int)

    df.drop_duplicates(inplace = True)
    return df

def yassify_data(df):
    df = df.copy()

    df.Age[df['Age'] == 1] = '18 to 24'
    df.Age[df['Age'] == 2] = '25 to 29'
    df.Age[df['Age'] == 3] = '30 to 34'
    df.Age[df['Age'] == 4] = '35 to 39'
    df.Age[df['Age'] == 5] = '40 to 44'
    df.Age[df['Age'] == 6] = '45 to 49'
    df.Age[df['Age'] == 7] = '50 to 54'
    df.Age[df['Age'] == 8] = '55 to 59'
    df.Age[df['Age'] == 9] = '60 to 64'
    df.Age[df['Age'] == 10] = '65 to 69'
    df.Age[df['Age'] == 11] = '70 to 74'
    df.Age[df['Age'] == 12] = '75 to 79'
    df.Age[df['Age'] == 13] = '80 or older'

    df.Diabetes_binary[df['Diabetes_binary'] == 0] = 'No Diabetes'
    df.Diabetes_binary[df['Diabetes_binary'] == 1] = 'Diabetes'

    df.HighBP[df['HighBP'] == 0] = 'No High'
    df.HighBP[df['HighBP'] == 1] = 'High BP'

    df.HighChol[df['HighChol'] == 0] = 'No High Cholesterol'
    df.HighChol[df['HighChol'] == 1] = 'High Cholesterol'

    df.CholCheck[df['CholCheck'] == 0] = 'No Cholesterol Check in 5 Years'
    df.CholCheck[df['CholCheck'] == 1] = 'Cholesterol Check in 5 Years'

    df.Smoker[df['Smoker'] == 0] = 'No'
    df.Smoker[df['Smoker'] == 1] = 'Yes'

    df.Stroke[df['Stroke'] == 0] = 'No'
    df.Stroke[df['Stroke'] == 1] = 'Yes'

    df.HeartDiseaseorAttack[df['HeartDiseaseorAttack'] == 0] = 'No'
    df.HeartDiseaseorAttack[df['HeartDiseaseorAttack'] == 1] = 'Yes'

    df.PhysActivity[df['PhysActivity'] == 0] = 'No'
    df.PhysActivity[df['PhysActivity'] == 1] = 'Yes'

    df.Fruits[df['Fruits'] == 0] = 'No'
    df.Fruits[df['Fruits'] == 1] = 'Yes'

    df.Veggies[df['Veggies'] == 0] = 'No'
    df.Veggies[df['Veggies'] == 1] = 'Yes'

    df.HvyAlcoholConsump[df['HvyAlcoholConsump'] == 0] = 'No'
    df.HvyAlcoholConsump[df['HvyAlcoholConsump'] == 1] = 'Yes'

    df.AnyHealthcare[df['AnyHealthcare'] == 0] = 'No'
    df.AnyHealthcare[df['AnyHealthcare'] == 1] = 'Yes'

    df.NoDocbcCost[df['NoDocbcCost'] == 0] = 'No'
    df.NoDocbcCost[df['NoDocbcCost'] == 1] = 'Yes'

    df.GenHlth[df['GenHlth'] == 5] = 'Excellent'
    df.GenHlth[df['GenHlth'] == 4] = 'Very Good'
    df.GenHlth[df['GenHlth'] == 3] = 'Good'
    df.GenHlth[df['GenHlth'] == 2] = 'Fair'
    df.GenHlth[df['GenHlth'] == 1] = 'Poor'

    df.DiffWalk[df['DiffWalk'] == 0] = 'No'
    df.DiffWalk[df['DiffWalk'] == 1] = 'Yes'

    df.Sex[df['Sex'] == 0] = 'Female'
    df.Sex[df['Sex'] == 1] = 'Male'

    df.Education[df['Education'] == 1] = 'Never Attended School'
    df.Education[df['Education'] == 2] = 'Elementary'
    df.Education[df['Education'] == 3] = 'Junior High School'
    df.Education[df['Education'] == 4] = 'Senior High School'
    df.Education[df['Education'] == 5] = 'Undergraduate Degree'
    df.Education[df['Education'] == 6] = 'Magister'

    df.Income[df['Income'] == 1] = 'Less Than $10,000'
    df.Income[df['Income'] == 2] = 'Less Than $10,000'
    df.Income[df['Income'] == 3] = 'Less Than $10,000'
    df.Income[df['Income'] == 4] = 'Less Than $10,000'
    df.Income[df['Income'] == 5] = 'Less Than $35,000'
    df.Income[df['Income'] == 6] = 'Less Than $35,000'
    df.Income[df['Income'] == 7] = 'Less Than $35,000'
    df.Income[df['Income'] == 8] = '$75,000 or More'

    return df

def create_plot_pivot(df, x_column):
    """ Create a pivot table for satisfaction versus another rating for easy plotting. """
    _df_plot = df.groupby([x_column, 'Diabetes_binary']).size() \
    .reset_index().pivot(columns='Diabetes_binary', index=x_column, values=0)
    return _df_plot