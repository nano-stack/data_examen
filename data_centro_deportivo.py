import pandas as pd
import numpy as np
import random

# -------------------- CONFIGURACIÓN --------------------
centros = ['Centro_Deportivo_1', 'Centro_Deportivo_2', 'Centro_Deportivo_3']
horas = np.arange(0, 24)
dias = pd.date_range(start="2025-05-01", end="2025-05-14", freq='D')  # 14 días
niveles = ['Alta', 'Media', 'Baja']

# -------------------- DATASET 1: uso_centros_deportivos.csv --------------------
uso_registros = []
for dia in dias:
    for hora in horas:
        for centro in centros:
            uso = np.random.poisson(lam=90 if centro == 'Centro_Deportivo_1' else 70 if centro == 'Centro_Deportivo_2' else 60)
            uso_registros.append([dia.date(), hora, centro, uso])

df_uso_centros = pd.DataFrame(uso_registros, columns=['Fecha', 'Hora', 'Centro', 'Cantidad_Usuarios'])

# Guardar CSV
df_uso_centros.to_csv("uso_centros_deportivos.csv", index=False)
