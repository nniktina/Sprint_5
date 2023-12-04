from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import locators


class TestRegistration:

    @staticmethod
    def reg_helper(driver, username_var, user_email_var, password_var):
        driver.find_element(By.XPATH, locators.reg_name).send_keys(username_var)
        driver.find_element(By.XPATH, locators.email).send_keys(user_email_var)
        driver.find_element(By.XPATH, locators.password).send_keys(password_var)
        driver.find_element(By.XPATH, locators.reg_button).click()

    def test_correct_data_successful_registration(self, username, user_email, correct_password, driver):
        driver.get(data.Urls.reg_page)
        TestRegistration.reg_helper(driver, username, user_email, correct_password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.enter_title)))
        driver.find_element(By.XPATH, locators.login_button).is_displayed()

    def test_wrong_password_failed_registration(self, username, user_email, incorrect_password, driver):
        driver.get(data.Urls.reg_page)
        TestRegistration.reg_helper(driver, username, user_email, incorrect_password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.error_pass)))
        assert driver.find_element(By.CSS_SELECTOR, locators.error_pass).text == "Некорректный пароль"
