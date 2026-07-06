# Proyecto de entrega final, Prueba de API
"https://jsonplaceholder.typicode.com/"

# Datos personales
    Autor: Carlos Ramirez
    Email: carlosara142@gmail.com

# El propósito del proyecto es validar el correcto funcionamiento de la página web asignada mediante el uso de las herramientas tecnológicas Pytest, Selenium y pytest-html. Se debe validar el inicio de sesión, el menú de la página, el catálogo de productos y su validación, así como la capacidad de agregar productos al carrito correctamente, validando el contador y el nombre de dicho artículo. Dentro de la carpeta de capturas se encuentra evidencia de resultados de test fallidos y excitosos.

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