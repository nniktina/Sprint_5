from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import locators


class TestRedirectToConstructor:

    @staticmethod
    def login_helper(driver):
        driver.find_element(By.XPATH, locators.email).send_keys(data.UserCredits.email)
        driver.find_element(By.XPATH, locators.password).send_keys(data.UserCredits.password)
        driver.find_element(By.XPATH, locators.login_button).click()

    def test_redirect_due_to_constructor_button(self, driver):
        driver.get(data.Urls.login_page)
        TestRedirectToConstructor.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_title)))
        driver.find_element(By.XPATH, locators.to_account).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.orders_history)))
        driver.find_element(By.XPATH, locators.constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.make_order)))
        assert driver.find_element(By.CSS_SELECTOR, locators.drag_the_bread).is_displayed()


    def test_redirect_due_to_logo_button(self, driver):
        driver.get(data.Urls.login_page)
        TestRedirectToConstructor.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_title)))
        driver.find_element(By.XPATH, locators.to_account).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.orders_history)))
        driver.find_element(By.CSS_SELECTOR, locators.main_logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.make_order)))
        assert driver.find_element(By.CSS_SELECTOR, locators.drag_the_bread).is_displayed()
