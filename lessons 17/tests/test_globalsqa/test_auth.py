from selenium.webdriver.common.by import By
import random
from ..conftest import *


class Test_Authorization:

    def test_valid_login(self, authorization):
        login_names = []
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        option_list = authorization.select_element(By.NAME, 'userSelect').options
        for names in option_list:
            login_names.append(names.text)
        random_login_choice = random.choice(login_names)
        authorization.select_element(By.NAME, 'userSelect').select_by_visible_text(random_login_choice)
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
        assert authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/strong').text == \
               f'Welcome {random_login_choice} !!'

    def test_invalid_login(self, authorization):
        login_names = []
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        option_list = authorization.select_element(By.NAME, 'userSelect').options
        for names in option_list:
            login_names.append(names.text)
        user_login_name = 'Serega Pushkin'
        assert user_login_name not in login_names

    def test_logout(self, authorization):
        login_names = []
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        option_list = authorization.select_element(By.NAME, 'userSelect').options
        for names in option_list:
            login_names.append(names.text)
        random_login_choice = random.choice(login_names)
        authorization.select_element(By.NAME, 'userSelect').select_by_visible_text(random_login_choice)
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
        authorization.search_element(By.CLASS_NAME, 'btn.logout').click()
        assert authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/form').is_displayed()
        assert authorization.driver.current_url == 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
