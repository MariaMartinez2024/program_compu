import pandas as pd
import numpy as np

# Cargar dataset Iris desde Kaggle (asegúrate de poner la ruta correcta)
df = pd.read_csv("program_compu/Iris.csv")

# Resumen estadístico
print("Resumen estadístico con describe():\n")
print(df.describe(include="all"))

# Tipos de datos
print("\nTipos de datos de cada columna:\n")
print(df.dtypes)

# Primeros y últimos registros
print("\nPrimeros registros con head():\n")
print(df.head())
print("\nÚltimos registros con tail():\n")
print(df.tail())

# Ordenar resultados (ejemplo: por SepalLengthCm)
print("\nOrdenando por SepalLengthCm:\n")
print(df.sort_values(by="SepalLengthCm", ascending=False).head())

# Medidas estadísticas en una columna
columna = "SepalLengthCm"

media = np.mean(df[columna])
mediana = np.median(df[columna])
desviacion = np.std(df[columna])

print(f"\nMedidas estadísticas de la columna {columna}:")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
