
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

    # ¿Bebedores empedernidos? (hombres adultos que toman mas de 14 tragos por semana y mujeres adultas que toman mas de 7 tragos por semana)
    ("AlcoholConsump", "number", "¿Cúantos tragos bebe por semana?", None, (0, 0, None, 1)),

    ("HighBP", "bin", "¿Tiene presion arterial alta?", None),
    ("HighChol", "bin", "¿Tiene colesterol alto?", None),
    ("Smoker", "bin", "¿Ha fumado al menos 100 cigarros en su vida entera?", None),
    ("Stroke", "bin", "¿(Alguna vez le dijeron) que tuvo un derrame cerebral?", None),
    ("HeartDiseaseorAttack", "bin", "¿Tiene enfermedad coronaria o infarto de miocardio?", None),
    ("PhysActivity", "bin", "¿Ha realizado actividad física en los ultimos 30 días? (Sin incluir el trabajo)", None),
    ("DiffWalk", "bin", "¿Tiene serias dificultades para caminar o subir escaleras?", None),

    ("GenHlth", "select", "¿Cómo diría que es su salud en general?", None, GenHlth_scale.keys()),
    ("MentHlth", "number", "¿Por cúantos de los últimos 30 días su salud mental no fue buena?", "Incluye estrés, depresión y problemas con las emociones", (0, 0, 30, 1)),
    ("PhysHlth", "number", "¿Por cúantos de los últimos 30 días su salud fisica no fue buena?", "Incluye enfermedades físicas y lesiones", (0, 0, 30, 1))
]

