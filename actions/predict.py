import time
import random

def predict(indicators):
    time.sleep(2)

    height = indicators["height"]
    weight = indicators["weight"]

    BMI = weight / (height**2)

    if BMI < 18.5:
        status = "Bajo de peso"
    elif BMI < 25.0:
        status = "Normal"
    elif BMI < 40:
        status = "Sobre peso"
    else: 
        status = "Obseo"
    
    return {
        "prediction": bool(random.getrandbits(1)),
        "BMI": BMI,
        "status": status
    }