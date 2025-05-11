
# Reporte de Pruebas de Rendimiento con Siege y Apache Benchmark (AB)

## Introducción

El objetivo de este reporte es presentar los resultados de las pruebas de rendimiento realizadas sobre el sistema de WordPress, utilizando herramientas de prueba de carga como **Siege** y **Apache Benchmark (AB)**. Las pruebas fueron realizadas en un entorno con múltiples nodos de base de datos y balanceo de carga mediante **HAProxy**.

## Arquitectura del Sistema

El sistema está diseñado con un enfoque de **alta disponibilidad y escalabilidad horizontal**, distribuido en 10 contenedores Docker interconectados mediante una red `bridge` personalizada (`galera`). Esta arquitectura simula un entorno de producción con redundancia tanto en la capa de base de datos como en la capa web. A continuación, se describen los componentes:

### Componentes

- **3 Nodos de Base de Datos MariaDB (Galera Cluster):**
  - `dbnode1`, `dbnode2`, `dbnode3`
  - Configurados con replicación síncrona Galera para asegurar consistencia entre nodos.
  - Arranque controlado por scripts y `depends_on` en Docker Compose.

- **3 Servidores Web (WordPress):**
  - `webnode1`, `webnode2`, `webnode3`
  - Cada contenedor contiene una instalación de WordPress conectada al clúster Galera a través del balanceador `haproxy_db_master`.

- **2 Balanceadores de Base de Datos (HAProxy):**
  - `haproxy_db_master` y `haproxy_db_slave` (puertos 3307 y 3308)
  - Distribuyen las conexiones a los nodos de base de datos mediante round-robin y revisiones de estado (health checks).

- **2 Balanceadores de Aplicación Web (HAProxy):**
  - `haproxy_web` en puerto 80 (predeterminado)
  - `haproxy_web_slave` en puerto 8081 (uso alternativo)
  - Balancean las peticiones entrantes hacia los contenedores `webnode*`.

### Diagrama de Arquitectura

![Diagrama]([./A_diagram_illustrates_a_high-level_web_application.](https://github.com/OrbelinJimenezVazquez/Computo-de-alto-desempe-o/blob/main/3%20Parcial/Capturas/LoadBalancers.png))
## Herramientas Utilizadas

- **Siege**: Herramienta para realizar pruebas de carga y medir la eficiencia de las aplicaciones web.
- **Apache Benchmark (AB)**: Herramienta para evaluar el rendimiento de servidores web.

## Pruebas Realizadas

### Siege

#### Prueba con 50 usuarios durante 1 minuto:
```bash
siege -c 50 -t 1m http://localhost/
```

- Transactions: 18,666  
- Availability: 100.00%  
- Elapsed time: 59.05 s  
- Data transferred: 67.47 MB  
- Response time: 0.16 s  
- Transaction rate: 316.11 trans/sec  
- Throughput: 1.14 MB/s  
- Concurrency: 49.72  
- Failed transactions: 0  

#### Prueba con 100 usuarios durante 5 minutos:
```bash
siege -c 100 -t 5m http://localhost/
```

- Transactions: 44,002  
- Availability: 100.00%  
- Elapsed time: 299.21 s  
- Data transferred: 159.01 MB  
- Response time: 0.68 s  
- Transaction rate: 147.06 trans/sec  
- Throughput: 0.53 MB/s  
- Concurrency: 99.41  
- Failed transactions: 0  

#### Prueba con 500 usuarios durante 10 minutos:
```bash
siege -c 500 -t 10m http://localhost/
```

- Transactions: 2,784  
- Availability: 64.06%  
- Elapsed time: 17.32 s  
- Data transferred: 18.69 MB  
- Response time: 1.43 s  
- Transaction rate: 160.74 trans/sec  
- Throughput: 1.08 MB/s  
- Concurrency: 230.67  
- Failed transactions: 1,562  

### Apache Benchmark (AB)

#### Prueba con 100 peticiones y 10 concurrencias:
```bash
ab -n 100 -c 10 http://localhost/
```

- Tiempo total: 1.215 s  
- Peticiones completadas: 100  
- Peticiones fallidas: 0  
- Requests/sec: 82.29  
- Tiempo medio por petición: 121.5 ms  
- Transfer rate: 4056.13 KB/sec  

#### Prueba con 1000 peticiones y 50 concurrencias:
```bash
ab -n 1000 -c 50 http://localhost/
```

- Tiempo total: 11.169 s  
- Peticiones completadas: 1000  
- Peticiones fallidas: 0  
- Requests/sec: 89.53  
- Tiempo medio por petición: 558.4 ms  
- Transfer rate: 4412.99 KB/sec  

#### Prueba con 10,000 peticiones y 500 concurrencias:
```bash
ab -n 10000 -c 500 http://localhost/
```

- Tiempo total: 17.054 s  
- Peticiones completadas: 10,000  
- Respuestas válidas: 8,628  
- Requests/sec: 586.39  
- Tiempo medio por petición: 852.68 ms  
- Transfer rate: 4080.45 KB/sec  

## Conclusiones

- El sistema soporta una carga ligera a moderada con buenos niveles de disponibilidad y baja latencia.
- Con 500 usuarios concurrentes, el sistema empieza a mostrar signos de saturación, disminuyendo la disponibilidad y aumentando los fallos.
- Apache Benchmark mostró buena estabilidad con niveles bajos y medios de concurrencia, pero se presentaron errores en pruebas de alta carga.
- Se recomienda seguir ajustando el tamaño del clúster, optimizar configuración de Apache y bases de datos, y considerar caching.

---
