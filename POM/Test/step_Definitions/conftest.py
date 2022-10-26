import time

import json
import pytest
from pytest_bdd import given
from selenium import webdriver
import selenium.webdriver

#constants
#AUTOMATION_PAGE = 'https://automationteststore.com/'


@pytest.fixture()
def browser(request):
    b = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.quit()

