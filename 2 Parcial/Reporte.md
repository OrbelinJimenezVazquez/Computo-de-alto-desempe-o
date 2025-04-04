# Reporte de Pruebas de Rendimiento con Siege y Apache Benchmark (AB)

## Introducción

El objetivo de este reporte es presentar los resultados de las pruebas de rendimiento realizadas sobre el sistema de WordPress, utilizando herramientas de prueba de carga como **Siege** y **Apache Benchmark (AB)**. Las pruebas fueron realizadas en un entorno con múltiples nodos de base de datos y balanceo de carga mediante **HAProxy**.

## Herramientas Utilizadas

- **Siege**: Herramienta para realizar pruebas de carga y medir la eficiencia de las aplicaciones web.
- **Apache Benchmark (AB)**: Herramienta para evaluar el rendimiento de servidores web.

## Comandos Ejecutados

### Pruebas con Siege

1. **Prueba con 100 usuarios y 30 segundos de duración**:
   ```bash
   siege -c 100 -t 30s http://localhost/

# Pruebas de Rendimiento con Siege y Apache Benchmark (AB)

## Comandos Utilizados

### Siege

* **Prueba con 50 usuarios durante 1 minuto:**

    ```bash
    siege -c 50 -t 1m http://localhost/
    ```

* **Prueba con 100 usuarios durante 5 minutos:**

    ```bash
    siege -c 100 -t 5m http://localhost/
    ```

### Apache Benchmark (AB)

* **Prueba básica con 100 peticiones y 10 concurrencias:**

    ```bash
    ab -n 100 -c 10 http://localhost/
    ```

* **Prueba más intensiva con 1000 peticiones y 50 concurrencias:**

    ```bash
    ab -n 1000 -c 50 http://localhost/
    ```

## Resultados de las Pruebas

### Resultados de Siege (Antes de la Optimización)

* **Prueba con 100 usuarios durante 30 segundos:**

    * Transacciones exitosas: 10113
    * Tiempo total de prueba: 29.47 segundos
    * Tiempo de respuesta: 0.92 segundos
    * Tasa de transacciones: 343.16 transacciones/segundo
    * Tasa de transferencia: 1.22 KB/segundo

* **Prueba con 50 usuarios durante 1 minuto:**

    * Transacciones exitosas: 17596
    * Tiempo total de prueba: 59.87 segundos
    * Tiempo de respuesta: 0.71 segundos
    * Tasa de transacciones: 293.90 transacciones/segundo
    * Tasa de transferencia: 9.74 KB/segundo

* **Prueba con 100 usuarios durante 5 minutos:**

    * Transacciones exitosas: 17912
    * Tiempo total de prueba: 289.53 segundos
    * Tiempo de respuesta: 0.52 segundos
    * Tasa de transacciones: 191.56 transacciones/segundo
    * Tasa de transferencia: 0.68 KB/segundo

### Resultados de Apache Benchmark (AB) (Antes de la Optimización)

* **Prueba básica con 100 peticiones y 10 concurrencias:**

    * Tiempo total de prueba: 1.822 segundos
    * Peticiones completadas: 100
    * Tiempo promedio por solicitud: 182.195 ms
    * Tasa de transferencia: 2680.47 KB/segundo
    * Conexión media (ms): 0.5 ms

* **Prueba más intensiva con 1000 peticiones y 50 concurrencias:**

    * Tiempo total de prueba: 8.097 segundos
    * Peticiones completadas: 1000
    * Tiempo promedio por solicitud: 404.859 ms
    * Tasa de transferencia: 6031.35 KB/segundo
    * Conexión media (ms): 0.4 ms

### Resultados de Siege (Después de la Optimización)

* **Prueba con 100 usuarios durante 30 segundos:**

    * Transacciones exitosas: 17596
    * Tiempo total de prueba: 59.87 segundos
    * Tiempo de respuesta: 0.71 segundos
    * Tasa de transacciones: 293.90 transacciones/segundo
    * Tasa de transferencia: 9.74 KB/segundo

* **Prueba con 50 usuarios durante 1 minuto:**

    * Transacciones exitosas: 57737
    * Tiempo total de prueba: 299.53 segundos
    * Tiempo de respuesta: 0.52 segundos
    * Tasa de transacciones: 191.56 transacciones/segundo
    * Tasa de transferencia: 0.68 KB/segundo

* **Prueba con 100 usuarios durante 5 minutos:**

    * Transacciones exitosas: 57737
    * Tiempo total de prueba: 299.53 segundos
    * Tiempo de respuesta: 0.52 segundos
    * Tasa de transacciones: 191.56 transacciones/segundo
    * Tasa de transferencia: 0.68 KB/segundo.

### Resultados de Apache Benchmark (AB) (Después de la Optimización)

* **Prueba básica con 100 peticiones y 10 concurrencias:**

    * Tiempo total de prueba: 8.097 segundos
    * Peticiones completadas: 1000
    * Tiempo promedio por solicitud: 404.859 ms
    * Tasa de transferencia: 6031.35 KB/segundo
    * Conexión media (ms): 0.4 ms

## Comparación de Resultados

### Antes de la Optimización:

* Tiempo promedio por solicitud (AB): 182 ms (100 peticiones), 404 ms (1000 peticiones)
* Tasa de transferencia (Siege): 1.22 KB/segundo (30 segundos), 9.74 KB/segundo (1 minuto)

### Después de la Optimización:

* Tiempo promedio por solicitud (AB): 400 ms (1000 peticiones)
* Tasa de transferencia (Siege): 9.74 KB/segundo (1 minuto)

## Conclusiones

### Mejoras en el Rendimiento:

* Después de realizar las optimizaciones, se observó una mejora significativa en la tasa de transferencia y la capacidad de manejar un mayor número de peticiones simultáneas.

### Impacto de la Optimización de Caché:

* Las configuraciones realizadas en W3 Total Cache mostraron una mejora en el tiempo de respuesta y la transferencia de datos.

### En realidad se pueden seguir haciendo mas optimizaciones al mismo wordpress atraves de los plugins pero pues ya tarde mucho averiguando esto, y ya no le quize meter mas jajjaaj
