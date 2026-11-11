
import os
import warnings
from datetime import datetime
import base64
import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from Utils import utils
from allure_commons.types import AttachmentType
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    allure.dynamic.parameter("Browser", browser)

    driver = None

    if browser == "chrome":
        options = Options()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option(
            "excludeSwitches", ['enable-automation']
        )
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    warnings.simplefilter('ignore', ResourceWarning)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(utils.URL)

    # Guardar temporalmente el driver para utilizarlo en el hook
    request.config._selenium_driver = driver

    yield driver

    driver.quit()
    request.config._selenium_driver = None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:

        print("\n[DEBUG] El test falló. Capturando imagen...")
        # Obtener el driver desde los argumentos del test
        driver = getattr(item.config, "_selenium_driver", None)
        print(f"[DEBUG] Driver encontrado: {driver is not None}")
        if driver is not None:
            try:
                screenshot = driver.get_screenshot_as_png()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"{item.name}_{timestamp}.png"
                # Guardar imagen en Reports
                path = _capture_screenshot(screenshot, screenshot_name)
                print(f"[DEBUG] Imagen guardada en: {path}")
                # Adjuntar a Allure
                allure.attach(
                    screenshot,
                    name="Screenshot",
                    attachment_type=AttachmentType.PNG
                )
                # Adjuntar a pytest-html
                extras = list(getattr(report, "extras", []))
                screenshot_base64 = base64.b64encode(
                    screenshot
                ).decode("utf-8")
                extras.append(
                    pytest_html.extras.png(
                        screenshot_base64,
                        name="Screenshot"
                    )
                )
                report.extras = extras
                print("[DEBUG] Imagen adjuntada al reporte HTML y Allure.")
            except Exception as e:
                print(f"[DEBUG] ERROR al capturar imagen: {repr(e)}")


def _capture_screenshot(screenshot, name):
    project_root = os.path.dirname(os.path.abspath(__file__))
    reports_path = os.path.join(project_root, "POM", "Reports")
    os.makedirs(reports_path, exist_ok=True)
    name = name.replace("/", "_").replace("\\", "_")
    final_path = os.path.join(reports_path, name)
    with open(final_path, "wb") as file:
        file.write(screenshot)
    return final_path
