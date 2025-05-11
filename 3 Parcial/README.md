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
