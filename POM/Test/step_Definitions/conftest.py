import time

import json
import warnings

import pytest
from pytest_bdd import given
from selenium import webdriver
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
    driver.quit()
