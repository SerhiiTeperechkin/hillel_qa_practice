from selenium.webdriver.common.by import By
import time
from ..conftest import *
from ..verification_constants import Verification_Constants


class Test_Playground:

    def test_basic_auth_version(self, authorization):
        authorization.driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
        assert authorization.search_element(By.XPATH, '//*[@id="content"]/div/p').text == \
               Verification_Constants.BASIC_AUTH_VERSION.value

    def test_checkboxes(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()
        authorization.search_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()
        assert authorization.search_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').is_selected()

    def test_form_authentication(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
        authorization.search_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
        authorization.search_element(By.XPATH, '//*[@id="login"]/button').click()
        assert authorization.search_element(By.XPATH, '//*[@id="flash"]').is_displayed()

    def test_status_codes(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[42]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/a').click()
        status_code = authorization.driver.execute_script(
            "return window.performance.getEntries()[0]['responseStatus'];")
        assert status_code == 404

    def test_key_presses(self, authorization):
        key = 'f'
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[31]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="target"]').send_keys(f'{key}')
        assert authorization.search_element(By.XPATH, '//*[@id="result"]').text == f'You entered: {key.capitalize()}'

    def test_file_download(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[17]/a').click()
        dl_elemnt = authorization.search_element(By.XPATH, '//*[@id="content"]/div/a[39]')
        file_name = dl_elemnt.text
        if not os.path.isfile(fr"{os.getcwd()}\{file_name}"):
            dl_elemnt.click()
            time.sleep(1)
        else:
            os.remove(fr"{os.getcwd()}\{file_name}")
            dl_elemnt.click()
            time.sleep(1)

        assert os.path.isfile(fr'{os.getcwd()}\{file_name}')
