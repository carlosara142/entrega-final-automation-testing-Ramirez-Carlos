# Proyecto de entrega final, Prueba de API
"https://jsonplaceholder.typicode.com/"

# Datos personales
    Autor: Carlos Ramirez
    Email: carlosara142@gmail.com

# El propósito del proyecto es validar el correcto funcionamiento de la API asignada mediante el uso de las herramientas tecnológicas Pytest, Pytest-chec y pytest-html. Se debe validar el correcto intercambio de data mediantes las funciones de Request y la verificacion de dichas respuestas obtenidas. Dentro de la carpeta logs se puede ver evidencia del registro de los testrealizados.

# instalacion mediante terminal
 - pip instal pytest
 - pip instal pytest-check
 - pip instal requests

# Comando del terminal para ejecutar todas las pruebas
pytest 
"ya la generacion de reportes y funciones pytest estan pre configuradas en pytest.ini"

# Rutas para pruebas unitarias en el termianl #

# Validar el login
pytest tests/test_saucedemo.py::test_login -v



# Generar reporte HTML
pytest 
"ya la generacion de reportes estan pre configuradas en pytest.ini"