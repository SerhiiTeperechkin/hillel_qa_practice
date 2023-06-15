from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os
import pytest


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


class Helper:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def search_element(self, by, selector):
        return self.wait.until(EC.element_to_be_clickable((by, selector)))

    def select_element(self, by, selector):
        select = Select(self.search_element(by, selector))
        return select

    def wait_visible(self, by, selector):
        return self.wait.until(EC.visibility_of_element_located((by, selector)))