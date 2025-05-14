import pandas as pd
import os

print("Directorio actual:", os.getcwd())

# Leer el archivo CSV con el delimitador correcto
df = pd.read_csv(r"C:\Users\orbel_jlkj13s\Documents\Computo-de-alto-desempe-o\docs\data\GOOG.csv", encoding="latin1")

# Imprimir los nombres de las columnas para verificar
print("Columnas del DataFrame:", df.columns)

# Asegurarse de que las columnas tengan el formato correcto (en minúsculas y sin espacios extra)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('+', 'plus').str.replace('/', '_')

# Convertir la columna 'date' de string a datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Para fechas ya existentes

# Ordenar por la columna 'date'
df = df.sort_values(by="date")

# Crear el directorio si no existe
output_dir = "docs/data"
os.makedirs(output_dir, exist_ok=True)

# Guardar el archivo JSON en el formato adecuado
df.to_json(f"{output_dir}/google.json", orient="records", lines=False)  # Aquí aseguramos que esté bien formateado.

print("Archivo JSON generado correctamente.")
