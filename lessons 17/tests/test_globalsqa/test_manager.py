from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..conftest import *
from ..verification_constants import Verification_Constants
import allure


@allure.story('Test for ManagerPanel on globalsqa')
class Test_ManagerPanel:
    @allure.title('Add customer test')
    @allure.description('Checking for correct addition of customer')
    def test_add_customer(self, authorization):
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input').send_keys(
            'Serega')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input').send_keys(
            'Pushkin')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input').send_keys(
            '65125')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        authorization.wait.until(EC.alert_is_present())
        alert_text = authorization.driver.switch_to.alert.text
        authorization.driver.switch_to.alert.accept()
        assert alert_text == Verification_Constants.ADD_CUSTOMER.value

    @allure.title('Open account test')
    @allure.description('Checking for correct open account of customer')
    def test_open_account(self, authorization):
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input').send_keys(
            'Serega')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input').send_keys(
            'Pushkin')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input').send_keys(
            '65125')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        authorization.wait.until(EC.alert_is_present())
        authorization.driver.switch_to.alert.accept()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
        authorization.select_element(By.XPATH, '//*[@id="userSelect"]').select_by_visible_text('Serega Pushkin')
        authorization.select_element(By.XPATH, '//*[@id="currency"]').select_by_visible_text('Dollar')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        assert authorization.wait.until(EC.alert_is_present())
        authorization.driver.switch_to.alert.accept()

    @allure.title('Delete customer test')
    @allure.description('Check for correct deletion of customers from the table')
    def test_delete_customer(self, authorization):
        data = {'first_name': 'Serega',
                'second_name': 'Pushkin',
                'post_code': '65125'
                }
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input').send_keys(
            data['first_name'])
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input').send_keys(
            data['second_name'])
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input').send_keys(
            data['post_code'])
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        authorization.wait.until(EC.alert_is_present())
        authorization.driver.switch_to.alert.accept()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[3]').click()
        table = authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        result = []
        for i in rows:
            f_name = i.find_elements(By.TAG_NAME, 'td')[0].text
            s_name = i.find_elements(By.TAG_NAME, 'td')[1].text
            p_code = i.find_elements(By.TAG_NAME, 'td')[2].text
            result.append(f'{f_name} {s_name} {p_code}')
        delete_index = result.index(f'{data["first_name"]} {data["second_name"]} {data["post_code"]}')
        authorization.search_element(By.XPATH,
                       f'/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[{delete_index}]/td[5]/button').click()
        table_update = authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table')
        rows_update = table_update.find_elements(By.TAG_NAME, 'tr')
        assert rows[delete_index] not in rows_update
