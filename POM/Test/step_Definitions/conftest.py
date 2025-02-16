import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Definir la fixture 'browser'
#@pytest.fixture()
#def browser(request):
    # Crear un objeto Service para el chromedriver
    #service = Service(executable_path="..\\Drivers\\chromedriver.exe")
    #service = Service(executable_path="C:\\Users\\User\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")

    # Crear un objeto Options para el navegador (si es necesario agregar configuraciones)
    #options = Options()
    # Puedes agregar configuraciones como --headless si necesitas ejecutar sin interfaz gráfica
    # options.add_argument("--headless")

    # Crear el WebDriver pasando el servicio y las opciones
  #  driver = webdriver.Chrome(service=service)

 #   driver.implicitly_wait(10)
 #   driver.maximize_window()

    # Devolver el navegador para que pueda ser usado en los tests
#    yield driver

    # Cerrar el navegador después de la prueba
import selenium.webdriver



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
#
# @pytest.fixture()
# def browser():
#     #service = Service(executable_path="C:\\Users\\User\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
#
#     # b = webdriver.Chrome("..\\Drivers\\chromedriver.exe")
#     # b.implicitly_wait(10)
#     # b.maximize_window()
#     # yield b
#     # b.quit()
#     driver = webdriver.Chrome(service=service)
#     driver.get(AUTOMATION_PAGE)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# @pytest.fixture()
# def browser():
#
#
#     # Inicializamos el driver de Chrome usando el servicio configurado
#     driver = webdriver.Chrome(service=service)
#
#     # Abrimos la página de automatización y configuramos algunas opciones
#     driver.get(AUTOMATION_PAGE)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#
#     # Pasamos el driver a la prueba
#     yield driver
#
#     # Después de que termine la prueba, cerramos el navegador
#     driver.quit()

@pytest.fixture()
def browser(request):
    service = Service(executable_path="C:\\Users\\User\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    #b = webdriver.Chrome("..\\Drivers\\chromedriver.exe")
    driver.get(AUTOMATION_PAGE)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
