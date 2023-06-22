from selenium.webdriver.common.by import By
from ..conftest import *
from ..verification_constants import Verification_Constants
import allure


@allure.story('Test for uitestingplayground')
class Test_Playground:
    @allure.title('Text input test')
    @allure.description('Entering text into an edit field may not have effect')
    def test_text_input(self, authorization):
        authorization.driver.get('http://uitestingplayground.com/home')
        authorization.search_element(By.XPATH, '//*[@id="overview"]/div/div[2]/div[4]/h3/a').click()
        authorization.search_element(By.XPATH, '//*[@id="newButtonName"]').send_keys('Test123321')
        authorization.search_element(By.XPATH, '//*[@id="updatingButton"]').click()
        assert authorization.search_element(By.ID, 'updatingButton').text == Verification_Constants.TEXT_INPUT.value

    @allure.title('Load delay test')
    @allure.description('Ensure that a test is capable of waiting for a page to load')
    def test_load_delay(self, authorization):
        authorization.driver.get('http://uitestingplayground.com/home')
        authorization.search_element(By.XPATH, '//*[@id="overview"]/div/div[1]/div[4]/h3/a').click()
        assert authorization.search_element(By.CLASS_NAME, 'btn.btn-primary').is_displayed()
        assert authorization.search_element(By.CLASS_NAME, 'btn.btn-primary').text == \
               Verification_Constants.LOAD_DELAY.value

    @allure.title('Verify text test')
    @allure.description('Finding an element by displayed text has nuances')
    def test_verify_text(self, authorization):
        authorization.driver.get('http://uitestingplayground.com/home')
        authorization.search_element(By.XPATH, '//*[@id="overview"]/div/div[3]/div[3]/h3/a').click()
        assert authorization.search_element(By.XPATH, '/html/body/section/div/div[4]/span').text == \
               Verification_Constants.VERIFY_TEXT.value

    @allure.title('Client side delay test')
    @allure.description('Some elements may appear after client-side time consuming JavaScript calculations')
    def test_client_side_delay(self, authorization):
        authorization.driver.get('http://uitestingplayground.com/home')
        authorization.search_element(By.XPATH, '//*[@id="overview"]/div/div[2]/div[2]/h3/a').click()
        authorization.search_element(By.XPATH, '//*[@id="ajaxButton"]').click()
        element = authorization.search_element(By.CLASS_NAME, 'bg-success')
        authorization.driver.execute_script("arguments[0].click();", element)
        assert authorization.wait_visible(By.CLASS_NAME, 'bg-success').text == \
               Verification_Constants.CLIENT_SIDE_DELAY.value

    @allure.title('Click test')
    @allure.description('Event based click on an element may not always work')
    def test_click(self, authorization):
        authorization.driver.get('http://uitestingplayground.com/home')
        authorization.search_element(By.XPATH, '//*[@id="overview"]/div/div[2]/div[3]/h3/a').click()
        old_class_name = authorization.search_element(By.CLASS_NAME, 'btn.btn-primary').get_attribute('class')
        authorization.search_element(By.XPATH, '//*[@id="badButton"]').click()
        new_class_name = authorization.search_element(By.CLASS_NAME, 'btn.btn-success').get_attribute('class')
        assert old_class_name != new_class_name

    @allure.title('Dynamic ID test')
    @allure.description('Make sure you are not recording dynamic IDs of elements')
    def test_dynamic_id(self, authorization):
        authorization.driver.get('http://uitestingplayground.com/home')
        authorization.search_element(By.XPATH, '//*[@id="overview"]/div/div[1]/div[1]/h3/a').click()
        authorization.search_element(By.CLASS_NAME, 'btn.btn-primary').click()
        assert authorization.search_element(By.CLASS_NAME, 'btn.btn-primary').text == \
               Verification_Constants.DYNAMIC_ID.value
