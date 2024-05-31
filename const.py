
GenHlth_scale = {
    "Excelente": 1,
    "Muy buena": 2, 
    "Buena": 3,
    "Regular": 4,
    "Mala": 5
}

Education_scale = {
    "Nunca/Solo jardin": 1,
    "Primaria": 2,
    "Bachillerato (parcial)": 3,
    "Bachillerato (graduado)": 4,
    "Universidad/Tecnico (parcial)": 5,
    "Universidad/Tecnico (graduado)": 6
}

FORM_SCHEMA = [    
    # Para el calculo del BMI
    ("height", "number", "Altura (metros)", None, (1.6, 1.0, None, 0.1)),
    ("weight", "number", "Peso (kg)", None, (50.0, 1.0, None, 0.1)),    
    ("Sex", "select", "Sexo", None, ("Hombre", "Mujer")), # No se tomo al final, pero se require para calcular HvyAlcoholConsump
    ("Age", "number", "Edad", None, (18, 18, None, 1)),
    ("Education", "select", "Educación", None, Education_scale.keys()),
    ("Income", "number", "Ingreso (dolares)", None, (0.0, 0.0, None, 100.0)),


    ("GenHlth", "select", "¿Cómo diría que es su salud en general?", None, GenHlth_scale.keys()),

    # ¿Bebedores empedernidos? (hombres adultos que toman mas de 14 tragos por semana y mujeres adultas que toman mas de 7 tragos por semana)
    ("AlcoholConsump", "number", "¿Cúantos tragos bebe por semana?", None, (0, 0, None, 1)),
    ("MentHlth", "number", "¿Por cúantos de los últimos 30 días su salud mental no fue buena?", "Incluye estrés, depresión y problemas con las emociones", (0, 0, 30, 1)),
    ("PhysHlth", "number", "¿Por cúantos de los últimos 30 días su salud fisica no fue buena?", "Incluye enfermedades físicas y lesiones", (0, 0, 30, 1)),

    ("HighBP", "bin", "¿Tiene presion arterial alta?", None),
    ("HighChol", "bin", "¿Tiene colesterol alto?", None),
    ("Smoker", "bin", "¿Ha fumado al menos 100 cigarros en su vida entera?", None),
    ("Stroke", "bin", "¿(Alguna vez le dijeron) que tuvo un derrame cerebral?", None),
    ("HeartDiseaseorAttack", "bin", "¿Tiene enfermedad coronaria o infarto de miocardio?", None),
    ("PhysActivity", "bin", "¿Ha realizado actividad física en los ultimos 30 días? (Sin incluir el trabajo)", None),
    ("DiffWalk", "bin", "¿Tiene serias dificultades para caminar o subir escaleras?", None),
]


TITLE = "Diseño e Implementaión de una Aplicación para el Diagnostico y Detección Temprana de Diabetes Tipo 2"

ABSTRACT = "La diabetes tipo 2 es una enfermedad cronica que representa un desafío significativo para la salud publica mundial, con una prevalencia en aumento y graves riesgos para la salud. En paralelo, el avance tecnologico, especialmente en el campo del Machine Learning (ML), ofrece oportunidades para mejorar el diagnostico y tratamiento de enfermedades. Este estudio propone el desarrollo de un modelo de diagnostico de diabetes tipo 2 basado en ML y Deep Learning (DL), con el objetivo de proporcionar una herramienta precisa y temprana para la deteccion de esta enfermedad. Se utilizarán técnicas avanzadas de ML y DL para aprender de datos pasados y extraer características complejas, con el fin de crear un modelo que pueda ser implementado en una aplicacion web interactiva. Esta aplicación permitira a los usuarios ingresar síntomas relacionados con la diabetes tipo 2 y recibir una evaluacion de riesgo personalizada. Los resultados esperados incluyen un modelo preciso y funcional, así como una aplicacion web accesible que pueda mejorar la deteccion temprana y el tratamiento oportuno de la diabetes tipo 2, contribuyendo así a una atencion médica más efectiva y personalizada."


INTRODUCCION = "La diabetes tipo 2 es una enfermedad crónica que afecta a millones de personas en todo el mundo, con un aumento significativo en su prevalencia. Esta condición puede llevar a graves complicaciones de salud como ceguera, insuficiencia renal, y enfermedades cardiovasculares. El avance en tecnologías como el Machine Learning (ML) ofrece oportunidades para mejorar el diagnóstico y tratamiento de esta enfermedad."

JUSTIFICACION = "Las herramientas de ML pueden asistir a los profesionales de la salud en la prevención y diagnóstico de enfermedades, mejorando los servicios médicos. La integración de estas tecnologías en la práctica clínica promete una atención médica más personalizada y eficaz."

OBJECTIVOS = "El objetivo general del proyecto es diseñar e implementar una aplicación web basada en Machine Learning para diagnosticar y detectar tempranamente la diabetes tipo 2. Los objetivos específicos incluyen revisar los avances en ML para la detección de diabetes, desarrollar la arquitectura de la solución utilizando datos del BRFSS 2015, implementar una aplicación web intuitiva para evaluaciones de riesgo y validar la precisión del modelo y la funcionalidad de la aplicación."


ASPECTOS_TEORICOS = "Se emplearon técnicas de Machine Learning como Random Forest, Decision Tree, XGBoost, KNN, Gaussian Naive-Bayes y MLP Classifier. La metodología CRISP-ML guió el desarrollo en etapas de comprensión, preparación, modelado y evaluación de datos. Se utilizó SMOTE junto con RandomUnderSampler para manejar el desequilibrio de clases. La precisión y el recall se mejoraron mediante la optimización de hiperparámetros con GridSearchCV. La validación cruzada garantizó la robustez de los modelos."

ARQUITECTURA = "Las herramientas de ML pueden asistir a los profesionales de la salud en la prevención y diagnóstico de enfermedades, mejorando los servicios médicos. La integración de estas tecnologías en la práctica clínica promete una atención médica más personalizada y eficaz."

RESULTADOS = "El modelo Random Forest destacó con una precisión del 91.07%, optimizado junto con otros modelos mediante SMOTE y RandomUnderSampler. La API y la web interactiva permiten evaluar el riesgo de diabetes con alta precisión, cumpliendo todos los objetivos del proyecto y demostrando la viabilidad de estas soluciones en entornos clínicos"

RESULTADOS_TABLA = {
    "modelo": [
        "Random Forest",
        "Ensemble",
        "Decision Tree",
        "XGB Classifier",
        "KNN"
    ],
    "acurracy (%)": [
        90.62,
        88.06,
        87.05,
        80.18,
        79.73
    ],
    "precision (%)": [
        90.62,
        88.36,
        88.21,
        80.54,
        81.06
    ],
    "recall (%)": [
        91.07,
        88.06,
        87.05,
        80.18,
        79.72
    ]
}

CONCLUSIONES = "El proyecto demostró la efectividad del Machine Learning en la detección temprana de diabetes tipo 2.El modelo Random Forest fue el más destacado. La API y la web interactiva permiten evaluar el riesgo de diabetes con precisión. El proyecto cumplió sus objetivos, proporcionando una base sólida para futuras mejoras y validando estas soluciones en entornos clínicos. Se planifican encuestas al personal de salud para mejorar el prototipo."

