# Proyecto final de testing de API publica
"https://jsonplaceholder.typicode.com/"

# Datos personales
    Autor: Carlos Ramirez
    Email: carlosara142@gmail.com

# El propósito del proyecto es validar el correcto funcionamiento de la API asignada mediante el uso de las herramientas tecnológicas Pytest, pytest-check y pytest-html. Se debe validar el flujo de datos mediante los comandos de REQUEST(GET,

# instalacion mediante terminal
 - pip install pytest
 - pip install requests
 - pip install pytest-html
 - pip install pytest-check

# Comando del terminal para ejecutar todas las pruebas
pytest test/"aca se coloca el nombre del test"
ya las funciones de pytest y la generacion de logs y reportes entan preconfigurados en pytest.ini

# Rutas para pruebas unitarias en el termianl #

# Validar el login
pytest tests/test_saucedemo.py::test_login -v

# Test de catalogo de productos y validar productos
pytest tests/test_saucedemo.py::test_catalogo_productos -v

# test de agregar productos al carrito, validar contador del carrito y validar nombre del producto en el carrito

pytest tests/test_saucedemo.py::test_agregar_al_carrito -v

inventory_sidebar_link

# test de menu hamburguesa

pytest tests/test_saucedemo.py::test_menu_hamburguesa -v

# Generar reporte HTML
pytest "ruta de la prueba"
ya la generaciond de reporte html esta configurada en pytest.ini"