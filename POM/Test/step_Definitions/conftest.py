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

<<<<<<< HEAD
=======
import json
import warnings

>>>>>>> 2fa78c339105440924a5bb0d77d85a97438def7b
import pytest
from selenium import webdriver
<<<<<<< HEAD
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
=======
import selenium.webdriver
from selenium.webdriver.chrome.service import Service


#constants
AUTOMATION_PAGE = 'https://automationteststore.com/'


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#
#
# @pytest.fixture()
# def browser(request):
#
#     from selenium import webdriver
#     browser = request.config.getoption("--browser")
#     if browser == 'chrome':
#         # driver = webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver-win32\\chromedriver.exe")
#         service_obj = Service("..\\Drivers\\chromedriver.exe")
#         driver = webdriver.Chrome(service=service_obj)
#     elif browser == 'firefox':
#         # driver = webdriver.Firefox("C:\\Users\\User\\Desktop\\Automation_Practice\\jqueryui\\Drivers\\geckodriver.exe")
#         service_obj = Service("..\\Drivers\\geckodriver.exe")
#         driver = webdriver.Firefox(service=service_obj)
#     warnings.simplefilter('ignore', ResourceWarning)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield
#     driver.quit()

@pytest.fixture()
def browser():
    # b = webdriver.Chrome("..\\Drivers\\chromedriver.exe")
    # b.implicitly_wait(10)
    # b.maximize_window()
    # yield b
    # b.quit()
    driver = webdriver.Chrome()
    driver.get(AUTOMATION_PAGE)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
>>>>>>> 2fa78c339105440924a5bb0d77d85a97438def7b
    driver.quit()
