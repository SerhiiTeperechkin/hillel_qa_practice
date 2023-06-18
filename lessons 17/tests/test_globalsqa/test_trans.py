from selenium.webdriver.common.by import By
from ..conftest import *
from ..verification_constants import Verification_Constants


class Test_Transaction:

    def test_deposit(self, authorization):
        deposit_value = 5000
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        authorization.select_element(By.NAME, 'userSelect').select_by_visible_text('Ron Weasly')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
        current_balance = authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[2]').text
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[2]').click()
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input').send_keys(deposit_value)
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button').click()
        after_deposit_balance = authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[2]').text
        assert authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/span').text == 'Deposit Successful'
        assert int(current_balance) + deposit_value == int(after_deposit_balance)

    def test_invalid_withdrawal(self, authorization):
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        authorization.select_element(By.NAME, 'userSelect').select_by_visible_text('Ron Weasly')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
        current_balance = authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[2]').text
        if int(current_balance) == 0:
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[3]').click()
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input').send_keys(5000)
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button').click()
            assert authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/span').text == \
                   Verification_Constants.INVALID_WITHDRAWAL.value

    def test_valid_withdrawal(self, authorization):
        authorization.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        authorization.select_element(By.NAME, 'userSelect').select_by_visible_text('Ron Weasly')
        authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
        if int(authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[2]').text) == 0:
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[2]').click()
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input').send_keys(50000)
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button').click()
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[3]').click()
            authorization.wait.until(EC.text_to_be_present_in_element
                            ((By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/label'),
                             'Amount to be Withdrawn :'))
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input').send_keys(5000)
            authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button').click()
            assert authorization.search_element(By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/span').text == \
                   Verification_Constants.VALID_WITHDRAWAL.value
