import pandas as pd
import os

print("Directorio actual:", os.getcwd())

# Leer el archivo CSV
df = pd.read_csv(r"C:\Users\orbel_jlkj13s\Documents\Computo-de-alto-desempe-o\docs\data\GOOG.csv", encoding="latin1")

# Imprimir los nombres de las columnas para verificar
print("Columnas del DataFrame:", df.columns)

# Asegurarse de que las columnas tengan el formato correcto (en minúsculas y sin espacios extra)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('+', 'plus').str.replace('/', '_')

# Ordenar por la columna 'date' en lugar de 'season'
df['date'] = pd.to_datetime(df['date'])  # Asegurarse de que la columna 'date' sea tipo datetime
df = df.sort_values(by="date")

# Crear el directorio si no existe
output_dir = "docs/data"
os.makedirs(output_dir, exist_ok=True)

# Guardar el archivo JSON
df.to_json(f"{output_dir}/google.json", orient="records", lines=True)

print("Archivo JSON generado correctamente.")
