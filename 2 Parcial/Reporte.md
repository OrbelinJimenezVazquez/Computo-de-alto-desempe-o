# Reporte de Pruebas de Rendimiento con Siege y Apache Benchmark (AB)

## Introducción

El objetivo de este reporte es presentar los resultados de las pruebas de rendimiento realizadas sobre el sistema de WordPress, utilizando herramientas de prueba de carga como **Siege** y **Apache Benchmark (AB)**. Las pruebas fueron realizadas en un entorno con múltiples nodos de base de datos y balanceo de carga mediante **HAProxy**.

## Diagrama de arquitectura 
![Diagrama](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/file_0000000079d051f69ae9b1c7682aadca_conversation_id%3D67ef354a-ae34-8002-890b-1f11672714b7%26message_id%3D5e5d09cb-78c4-43c3-9e27-8867067886d7%20(1).PNG).


### Pruebas
![Pruebas](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Screenshot%20at%202025-04-03%2019-29-27.png).
![Pruebas](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Screenshot%20at%202025-04-03%2023-07-22.png ).
![Pruebas]( https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Screenshot%20at%202025-04-03%2023-18-56.png).
![Pruebas](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Screenshot%20at%202025-04-03%2023-25-54.png ).

## Herramientas Utilizadas

- **Siege**: Herramienta para realizar pruebas de carga y medir la eficiencia de las aplicaciones web.
- **Apache Benchmark (AB)**: Herramienta para evaluar el rendimiento de servidores web.

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

### Resultados de Siege (Después de la Optimización)

* **Prueba con 50 usuarios durante 1 minuto:**

    * Transacciones exitosas: 29687
    * Tiempo total de prueba: 59.29 segundos
    * Tiempo de respuesta: 0.10 segundos
    * Tasa de transacciones: 500.71 transacciones/segundo
    * Tasa de transferencia: 1.77 KB/segundo

    ![Prueba con 50 usuarios durante 1 minuto - Siege](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Prueba%20con%2050%20usuarios%20durante%201%20minuto_Siege.png)

* **Prueba con 100 usuarios durante 5 minutos:**

    * Transacciones exitosas: 144725
    * Tiempo total de prueba: 299.61 segundos
    * Tiempo de respuesta: 0.21 segundos
    * Tasa de transacciones: 483.04 transacciones/segundo
    * Tasa de transferencia: 1.71 KB/segundo

    ![Prueba con 100 usuarios durante 5 minutos - Siege](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Prueba%20con%20100%20usuarios%20durante%205%20minutos_.png)

### Resultados de Apache Benchmark (AB) (Después de la Optimización)

* **Prueba básica con 100 peticiones y 10 concurrencias:**

    * Tiempo total de prueba: 0.696 segundos
    * Peticiones completadas: 100
    * Tiempo promedio por solicitud: 6.965 ms
    * Tasa de transferencia: 6996.35 KB/segundo
    * Conexión media (ms): 0.5 ms

    ![Prueba básica con 100 peticiones y 10 concurrencias - AB](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Prueba%20b%C3%A1sica%20con%20100%20peticiones%20y%2010%20concurrencias.png)

* **Prueba más intensiva con 1000 peticiones y 50 concurrencias:**

    * Tiempo total de prueba: 6.627 segundos
    * Peticiones completadas: 1000
    * Tiempo promedio por solicitud: 331.375 ms
    * Tasa de transferencia: 7352.48 KB/segundo
    * Conexión media (ms): 0.3 ms

    ![Prueba más intensiva con 1000 peticiones y 50 concurrencias - AB](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/Prueba%20m%C3%A1s%20intensiva%20con%201000%20peticiones%20y%2050%20concurrencias_.png)

## Comparación de Resultados

### Antes de la Optimización:

* **Siege:**
    * Prueba con 50 usuarios durante 1 minuto:
        * Transacciones exitosas: 17596
        * Tiempo de respuesta: 0.71 segundos
        * Tasa de transacciones: 293.90 transacciones/segundo
        * Tasa de transferencia: 9.74 KB/segundo
        * ![Prueba](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/prueba2.1.1siege.png).
    * Prueba con 100 usuarios durante 5 minutos:
        * Transacciones exitosas: 17912
        * Tiempo de respuesta: 0.52 segundos
        * Tasa de transacciones: 191.56 transacciones/segundo
        * Tasa de transferencia: 0.68 KB/segundo
        * ![Prueba](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/prueba2.1.1siege.png).

* **AB:**
    * Prueba básica con 100 peticiones y 10 concurrencias:
        * Tiempo promedio por solicitud: 182.195 ms
        * Tasa de transferencia: 2680.47 KB/segundo
       * ![Prueba](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/prueba2.1ab.png).
      
    * Prueba más intensiva con 1000 peticiones y 50 concurrencias:
        * Tiempo promedio por solicitud: 404.859 ms
        * Tasa de transferencia: 6031.35 KB/segundo
         * ![Prueba](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/prueba1.1ab.png).

### Después de la Optimización:

* **Siege:**
    * Prueba con 50 usuarios durante 1 minuto:
        * Transacciones exitosas: 29687
        * Tiempo de respuesta: 0.10 segundos
        * Tasa de transacciones: 500.71 transacciones/segundo
        * Tasa de transferencia: 1.77 KB/segundo
    * Prueba con 100 usuarios durante 5 minutos:
        * Transacciones exitosas: 144725
        * Tiempo de respuesta: 0.21 segundos
        * Tasa de transacciones: 483.04 transacciones/segundo
        * Tasa de transferencia: 1.71 KB/segundo

* **AB:**
    * Prueba básica con 100 peticiones y 10 concurrencias:
        * Tiempo promedio por solicitud: 6.965 ms
        * Tasa de transferencia: 6996.35 KB/segundo
    * Prueba más intensiva con 1000 peticiones y 50 concurrencias:
        * Tiempo promedio por solicitud: 331.375 ms
        * Tasa de transferencia: 7352.48 KB/segundo

## Conclusiones

### Mejoras en el Rendimiento:

* Se observó una mejora significativa en la tasa de transferencia y en la capacidad de manejar un mayor número de peticiones simultáneas.

### Impacto de la Optimización de Caché:

* Las configuraciones realizadas en W3 Total Cache mostraron una mejora en el tiempo de respuesta y la transferencia de datos.

### Recomendaciones:

* Continuar con las optimizaciones de caché y considerar el uso de herramientas avanzadas como Redis o Memcached para mejorar aún más el rendimiento.
* Realizar pruebas periódicas de rendimiento a medida que el tráfico crece para asegurar la escalabilidad y estabilidad del sistema.

### Mejoras en el Rendimiento:

* Después de realizar las optimizaciones, se observó una mejora significativa en la tasa de transferencia y la capacidad de manejar un mayor número de peticiones simultáneas.

### Impacto de la Optimización de Caché:

* Las configuraciones realizadas en W3 Total Cache mostraron una mejora en el tiempo de respuesta y la transferencia de datos.

* ![Comparaciones](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/comparacione_Siege50.png).
* ![Comparaciones](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/comparaciones_Siege100.png).
* ![Comparaciones](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/comparaciones_ab100.png)
* ![Comparaciones](https://github.com/OrbelinJimnez/Computo-de-alto-desempe-o/blob/main/2%20Parcial/Capturas/comparaciones_ab1000.png)


### En realidad se pueden seguir haciendo mas optimizaciones al mismo wordpress atraves de los plugins pero pues ya tarde mucho averiguando esto, y ya no le quize meter mas jajjaaj
