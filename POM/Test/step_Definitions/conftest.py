import base64
import os
import warnings
from datetime import datetime
import re
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from allure_commons.types import AttachmentType
import allure

from Utils import utils

# URL de la aplicación
#URL = "https://automationteststore.com/"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Navegador a usar: chrome o firefox")


# -------------------------------
# Fixture de setup de test
# -------------------------------
@pytest.fixture(scope="function")
def test_setup(request):
    browser_name = request.config.getoption("--browser")
    driver = None

    if browser_name.lower() == "chrome":
        options = Options()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        driver = webdriver.Chrome(options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    warnings.simplefilter('ignore', ResourceWarning)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(utils.URL)

    yield driver
    driver.quit()


# -------------------------------
# Hook para capturar screenshots en caso de fallo
# -------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("call", "setup") and report.failed:
        driver = None
        try:
            driver = item.funcargs.get("test_setup") or item._request.getfixturevalue("test_setup")
        except Exception:
            pass

        # Crear carpeta Reports
        reports_dir = os.path.join(os.getcwd(), "Reports")
        os.makedirs(reports_dir, exist_ok=True)

        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_nodeid = re.sub(r'[^0-9a-zA-Z_]+', '_', report.nodeid)
            screenshot_name = f"{safe_nodeid}_{timestamp}.png"
            screenshot_path = os.path.join(reports_dir, screenshot_name)

            # Guardar screenshot
            driver.save_screenshot(screenshot_path)

            # Adjuntar a Allure
            allure.attach(driver.get_screenshot_as_png(),
                          name="Screenshot", attachment_type=AttachmentType.PNG)

            # Adjuntar a pytest-html
            extra = getattr(report, "extra", [])
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                try:
                    with open(screenshot_path, "rb") as f:
                        image_bytes = f.read()
                    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
                    extra.append(pytest_html.extras.image(image_base64, mime_type="image/png"))
                except Exception as e:
                    print(f"[SCREENSHOT] No se pudo adjuntar screenshot en pytest-html: {e}")
            report.extra = extra
        else:
            print("[SCREENSHOT] No se pudo capturar screenshot: driver no disponible")


# -------------------------------
# Función auxiliar para capturas manuales
# -------------------------------
def _capture_screenshot(driver, name):
    reports_path = os.path.join(os.getcwd(), "Reports")
    os.makedirs(reports_path, exist_ok=True)
    final_path = os.path.join(reports_path, name)
    driver.save_screenshot(final_path)
    return final_path