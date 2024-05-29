import requests
from const import GenHlth_scale, Education_scale

# API_BASE_URL = "http://127.0.0.1:8000"
API_BASE_URL = "https://apps-sonya-wins-7572706e.koyeb.app/"

def predict(features):
    body = {}

    # Compute BMI 
    height = features["height"]
    weight = features["weight"]

    BMI = weight / (height**2)

    if BMI < 18.5: status = "Bajo de peso"
    elif BMI < 25.0: status = "Normal"
    elif BMI < 40: status = "Sobre peso"
    else: status = "Obseo"

    body["BMI"] = BMI
    
    # Compute HvyAlcoholConsump
    # ¿Bebedores empedernidos? (hombres adultos que toman mas de 14 tragos por semana y mujeres adultas que toman mas de 7 tragos por semana)
    sex = features["Sex"]
    alcoholConsump = features["AlcoholConsump"]
    body["HvyAlcoholConsump"] = int((sex == "Hombre" and alcoholConsump > 14) or (sex == "Mujer" and alcoholConsump > 7))

    # Binary and numeric data 
    feats_to_int = ["HighBP", "HighChol","Smoker","Stroke","HeartDiseaseorAttack","PhysActivity","DiffWalk", "MentHlth", "PhysHlth"]
    for feat_name in feats_to_int:
        body[feat_name] = int(features[feat_name])

    # GenHlth
    body["GenHlth"] = GenHlth_scale[features["GenHlth"]]
    
    # Age
    age = features["Age"]
    
    if 18 <= age <= 24: age_category = 1
    elif 25 <= age <= 29: age_category = 2
    elif 30 <= age <= 34: age_category = 3
    elif 35 <= age <= 39: age_category = 4
    elif 40 <= age <= 44: age_category = 5
    elif 45 <= age <= 49: age_category = 6
    elif 50 <= age <= 54: age_category = 7
    elif 55 <= age <= 59: age_category = 8
    elif 60 <= age <= 64: age_category = 9
    elif 65 <= age <= 69: age_category = 10
    elif 70 <= age <= 74: age_category = 11
    elif 75 <= age <= 79: age_category = 12
    elif age >= 80: age_category = 13
    else: age_category = 0 

    body["Age"] = age_category

    # Education
    body["Education"] = Education_scale[features["Education"]]
    
    # Income
    income = float(features["Income"])
    if income < 10000: income_category = 1
    elif 10000 <= income < 15000: income_category = 2
    elif 15000 <= income < 20000: income_category = 3
    elif 20000 <= income < 25000: income_category = 4
    elif 25000 <= income < 35000: income_category = 5
    elif 35000 <= income < 50000: income_category = 6
    elif 50000 <= income < 75000: income_category = 7
    elif income >= 75000: income_category = 8
    else: income_category = 0

    body["Income"] = income_category

    response = requests.post(
        f"{API_BASE_URL}/predict",
        json=body
    )
    
    print(response.status_code)

    if response.status_code != 200:
        raise Exception(f"Key error. response code = {response.status_code}")
    
    data = response.json()

    return {
        "prediction": bool(data["diabetes_prediction"]),
        "BMI": BMI,
        "status": status
    }