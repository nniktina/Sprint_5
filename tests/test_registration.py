from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data


class TestRegistration:

    @staticmethod
    def reg_helper(driver, username, user_email, correct_password):
        driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(username)
        driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(user_email)
        driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(correct_password)
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    def test_correct_data_successful_registration(self, driver, username, user_email, correct_password):
        driver.get(data.Urls.reg_page)
        TestRegistration.reg_helper(driver, username, user_email, correct_password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(By.XPATH, './/button[text()="Войти"]').is_displayed()

    def test_wrong_password_failed_registration(self, driver, username, user_email, incorrect_password):
        driver.get(data.Urls.reg_page)
        TestRegistration.reg_helper(driver, username, user_email, incorrect_password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.input__error')))
        assert driver.find_element(By.CSS_SELECTOR, '.input__error').text == "Некорректный пароль"
