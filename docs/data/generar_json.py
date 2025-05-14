import pandas as pd
import os

print("Directorio actual:", os.getcwd())

# Leer el archivo CSV de Google
df = pd.read_csv("C:/Users/orbel_jlkj13s/Documents/Computo-de-alto-desempe-o/docs/data/GOOG.csv", encoding="latin1")

# Limpiar los nombres de las columnas (en minúsculas, sin espacios y caracteres especiales)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('+', 'plus').str.replace('/', '_')

# Asegurarse de que la columna 'date' sea tipo datetime y ordenarlo por esta columna
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Convertir 'date' a datetime
df = df.sort_values(by="date")

# Crear el directorio si no existe
output_dir = "docs/data"
os.makedirs(output_dir, exist_ok=True)

# Guardar el archivo JSON
df.to_json(f"{output_dir}/google_clean.json", orient="records", lines=True)

print("Archivo JSON generado correctamente.")
