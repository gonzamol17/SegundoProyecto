from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

AUTOMATION_PAGE = 'https://automationteststore.com/'

@pytest.fixture()
def browser(request):
    current_directory = Path(__file__).parent.parent
    driver_path = current_directory.parent.parent / "Drivers" / "chromedriver.exe"
    service = Service(executable_path=str(driver_path))
    driver = webdriver.Chrome(service=service)
    driver.get(AUTOMATION_PAGE)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
