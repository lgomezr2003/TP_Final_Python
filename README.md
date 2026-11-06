# TP_Final_Python
##Repositorio donde subo los ejercicios finales del curso de Python
Este repositorio contiene la resolución de los tres ejercicios prácticos integradores del curso, aplicando conceptos de modularización, programación orientada a objetos (POO), manejo de excepciones, persistencia de datos, testing unitario y desarrollo web con Django.
Estructura del Repositorio

El proyecto está dividido en tres carpetas independientes, una por cada ejercicio:

├── Ejercicio1/   # Organizador de archivos y limpieza de sensores
├── Ejercicio2/   # Modelo de productos e inventario
└── Ejercicio3/   # Auditoría con tests y web con Django

Requisitos Previos Globales:
Para probar los ejercicios, necesitas tener instalado Python 3.10+ y Git. Se recomienda enfáticamente crear un entorno virtual para cada ejercicio para no mezclar dependencias.

A continuación, las instrucciones de ejecución para cada apartado.


##Ejercicio 1: Organizador y Monitor de Sensores

Ubicación: /Ejercicio1

Este ejercicio consta de dos partes: un organizador de archivos por extensión y un procesador de métricas de sensores desde un archivo JSON.
1. Instalación de dependencias

Ingresá a la carpeta, creá un entorno virtual y instalá los requerimientos:


cd Ejercicio1
python3 -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requeriments.txt

2. Limpieza y monitoreo de sensores

El programa lee un archivo crudo (ubicado en datos/registros_raw.json), sanitiza los datos, guarda una versión limpia y genera un reporte de alertas por temperatura.


**python main.py datos/registros_raw.json -o datos/salida_clean.json -u 22.0**

Parámetros:

    -o: Ruta de salida del JSON limpio.

    -u: Umbral de temperatura para las alertas (default: 22.0).


##Ejercicio 2: Catálogo de Inventario EcoTech

Ubicación: /Ejercicio2

Modelado orientado a objetos con encapsulamiento, excepciones personalizadas y persistencia en JSON.
1. Ejecución

Este ejercicio no requiere librerías externas (solo Python puro).
bash

cd Ejercicio2
source venv/bin/activate
**python3 main.py**

2. ¿Qué hace el script?

    Crea dispositivos (Paneles Solares y una Batería).

    Intenta asignar un stock negativo y captura la excepción StockInvalidoError exitosamente.

    Exporta los productos válidos a un archivo JSON en datos/catalogo_ecotech.json.

    Imprime por consola las fichas técnicas con polimorfismo.


##Ejercicio 3: Auditoría y Panel Web Django

Ubicación: /Ejercicio3

Auditoría de un algoritmo de emisiones mediante tests unitarios e integración del mismo en una vista web con Django.
1. Instalación de dependencias

cd Ejercicio3
python3 -m venv venv
source venv/bin/activate
pip install django

2. Ejecutar Tests Unitarios (Auditoría)

Para verificar la exactitud del cálculo de huella de carbono:

**python -m unittest discover tests -v**

Salida esperada: 6 pruebas exitosas (OK).

3. Levantar el servidor web

Iniciá el servidor de desarrollo de Django:


**python manage.py runserver**

Luego, abrí tu navegador e ingresá a la siguiente URL:
<http://127.0.0.1:8000/sustentabilidad/panel/>

Verás una tabla renderizada con el total de emisiones y el detalle por planta industrial.
