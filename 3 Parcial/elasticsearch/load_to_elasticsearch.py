from elasticsearch import Elasticsearch
import pandas as pd

# Conectar con Elasticsearch especificando el esquema http
es = Elasticsearch([{'host': 'localhost', 'port': 9201, 'scheme': 'http'}])

# Cargar el dataset (asegúrate de que el archivo CSV esté en la misma carpeta que este script)
df = pd.read_csv('Google_Stock_Price.csv')

# Indexar cada fila en Elasticsearch
for index, row in df.iterrows():
    doc = row.to_dict()
    es.index(index="google_stock_price", document=doc)

