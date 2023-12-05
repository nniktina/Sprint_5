from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import locators


class TestLogin:

    @staticmethod
    def login_helper(driver):
        driver.find_element(By.XPATH, locators.email).send_keys(data.UserCredits.email)
        driver.find_element(By.XPATH, locators.password).send_keys(data.UserCredits.password)
        driver.find_element(By.XPATH, locators.login_button).click()

    def test_login_from_main_page_successful(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, locators.login_to_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(data.Urls.login_page))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_title)))
        assert driver.find_element(By.CSS_SELECTOR, locators.burger_assemble).is_displayed()

    def test_login_from_personal_account_button(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, locators.to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.Urls.login_page))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_title)))
        assert driver.find_element(By.CSS_SELECTOR, locators.burger_assemble).is_displayed()

    def test_login_from_registration_page(self, driver):
        driver.get(data.Urls.reg_page)
        driver.find_element(By.CSS_SELECTOR, locators.login_from_reg_and_forgot).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.Urls.login_page))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_title)))
        assert driver.find_element(By.CSS_SELECTOR, locators.burger_assemble).is_displayed()

    def test_login_from_password_forgot_page(self, driver):
        driver.get(data.Urls.forgot_pass)
        driver.find_element(By.CSS_SELECTOR, locators.login_from_reg_and_forgot).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.Urls.login_page))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_title)))
        assert driver.find_element(By.CSS_SELECTOR, locators.burger_assemble).is_displayed()