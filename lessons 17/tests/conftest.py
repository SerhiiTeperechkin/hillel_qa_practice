from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import pytest
from .helper import Helper


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": f"{os.getcwd()}",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def wait(driver):
    wait = WebDriverWait(driver, timeout=20, poll_frequency=1)
    yield wait


@pytest.fixture(scope='session')
def authorization(driver, wait):
    return Helper(driver, wait)

