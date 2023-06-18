from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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