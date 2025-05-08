encuestas = []
for centro in centros:
    for _ in range(80):
        global_satisf = random.choices(niveles, weights=[0.3, 0.5, 0.2])[0]
        instalaciones = random.choices(niveles, weights=[0.3, 0.5, 0.2])[0]
        banos = random.choices(niveles, weights=[0.25, 0.5, 0.25])[0]
        atencion = random.choices(niveles, weights=[0.3, 0.4, 0.3])[0]
        encuestas.append([
            centro,
            global_satisf,
            instalaciones,
            banos,
            atencion
        ])

df_encuestas = pd.DataFrame(encuestas, columns=[
    'Centro', 'Satisfaccion_Global', 'Satisfaccion_Instalaciones',
    'Satisfaccion_Banos', 'Satisfaccion_Atencion'
])

df_encuestas.to_csv("encuestas_centros_deportivos.csv", index=False)

# -------------------- DATASET 3: capacidad_centros_deportivos.csv --------------------
capacidad = {
    'Centro_Deportivo_1': 300,
    'Centro_Deportivo_2': 250,
    'Centro_Deportivo_3': 200
}

df_capacidad = pd.DataFrame(list(capacidad.items()), columns=['Centro', 'Capacidad_Usuarios'])
df_capacidad.to_csv("capacidad_centros_deportivos.csv", index=False)

print("✅ Archivos CSV generados correctamente.")
