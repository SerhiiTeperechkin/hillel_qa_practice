from selenium.webdriver.common.by import By
import time
from ..conftest import *
from ..verification_constants import Verification_Constants
import allure


@allure.story('Test for the-internet.herokuapp')
class Test_HerokuApp:
    @allure.title('Basic Auth Version test')
    @allure.description('Using (user and pass: admin) to login')
    def test_basic_auth_version(self, authorization):
        authorization.driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
        assert authorization.search_element(By.XPATH, '//*[@id="content"]/div/p').text == \
               Verification_Constants.BASIC_AUTH_VERSION.value

    @allure.title('Checkboxes test')
    @allure.description('Click to checkboxes and check is it selected')
    def test_checkboxes(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()
        authorization.search_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()
        assert authorization.search_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').is_selected()

    @allure.title('Form Authentication test')
    @allure.description('Authentication in form using login and password and checked for success auth')
    def test_form_authentication(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
        authorization.search_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
        authorization.search_element(By.XPATH, '//*[@id="login"]/button').click()
        assert authorization.search_element(By.XPATH, '//*[@id="flash"]').is_displayed()

    @allure.title('Status code test')
    @allure.description('Checked that status code : 404')
    def test_status_codes(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[42]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/a').click()
        status_code = authorization.driver.execute_script(
            "return window.performance.getEntries()[0]['responseStatus'];")
        assert status_code == 404

    @allure.title('Key presses test')
    @allure.description('Check that the button we pressed is displayed correctly')
    def test_key_presses(self, authorization):
        key = 'f'
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[31]/a').click()
        authorization.search_element(By.XPATH, '//*[@id="target"]').send_keys(f'{key}')
        assert authorization.search_element(By.XPATH, '//*[@id="result"]').text == f'You entered: {key.capitalize()}'

    @allure.title('File download test')
    @allure.description('Download the file and check for the correctness of the downloaded file')
    def test_file_download(self, authorization):
        authorization.driver.get('http://the-internet.herokuapp.com/')
        authorization.search_element(By.XPATH, '//*[@id="content"]/ul/li[17]/a').click()
        dl_elemnt = authorization.search_element(By.XPATH, '//*[@id="content"]/div/a[2]')
        file_name = dl_elemnt.text
        if not os.path.isfile(fr"{os.getcwd()}\{file_name}"):
            dl_elemnt.click()
            time.sleep(1)
        else:
            os.remove(fr"{os.getcwd()}\{file_name}")
            dl_elemnt.click()
            time.sleep(1)

        assert os.path.isfile(fr'{os.getcwd()}\{file_name}')
