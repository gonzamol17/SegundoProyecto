import time
#
# import json
# import pytest
# from pytest_bdd import given
# from selenium import webdriver
# import selenium.webdriver
#
# #constants
# #AUTOMATION_PAGE = 'https://automationteststore.com/'
#
#
# @pytest.fixture()
# def browser(request):
#     b = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")
#     b.implicitly_wait(10)
#     b.maximize_window()
#     yield b
#     b.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Definir la fixture 'browser'
@pytest.fixture()
def browser(request):
    # Crear un objeto Service para el chromedriver
    #service = Service(executable_path="..\\Drivers\\chromedriver.exe")
    service = Service(executable_path="C:\\Users\\User\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")

    # Crear un objeto Options para el navegador (si es necesario agregar configuraciones)
    #options = Options()
    # Puedes agregar configuraciones como --headless si necesitas ejecutar sin interfaz gráfica
    # options.add_argument("--headless")

    # Crear el WebDriver pasando el servicio y las opciones
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(10)
    driver.maximize_window()

    # Devolver el navegador para que pueda ser usado en los tests
    yield driver

    # Cerrar el navegador después de la prueba
    driver.quit()
