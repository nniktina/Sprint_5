from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import locators

class TestLogout:
    def test_logout_after_login(self, driver):
        driver.get(data.Urls.login_page)
        driver.find_element(By.XPATH, locators.email).send_keys(data.UserCredits.email)
        driver.find_element(By.XPATH, locators.password).send_keys(data.UserCredits.password)
        driver.find_element(By.XPATH, locators.login_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_title)))
        driver.find_element(By.XPATH, locators.to_account).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.orders_history)))
        driver.find_element(By.XPATH, locators.logout_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locators.reg_from_login)))

        assert driver.find_element(By.XPATH, locators.login_button).is_displayed()
