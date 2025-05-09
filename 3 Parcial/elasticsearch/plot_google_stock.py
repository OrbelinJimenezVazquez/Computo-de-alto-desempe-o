from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt

# Conectar con Elasticsearch especificando el esquema (http o https)
es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9201}])

# Definir el query para obtener los datos
query = {
    "query": {
        "match_all": {}
    }
}

# Buscar los datos en Elasticsearch
response = es.search(index="google_stock_price", body=query)

# Extraer los datos del 'hits' de la respuesta
data = [hit['_source'] for hit in response['hits']['hits']]

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Asegúrate de que las columnas estén correctamente nombradas
df['date'] = pd.to_datetime(df['date'])  # Asegúrate de convertir 'date' en un tipo datetime

# Graficar el precio de cierre (close)
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['close'], label='Google Stock Price', color='blue')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.title('Google Stock Price Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar la imagen como un archivo PNG
plt.savefig('google_stock_price_plot.png')
# Mostrar la gráfica
plt.show()
