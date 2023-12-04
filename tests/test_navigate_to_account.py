from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import locators


class TestNavigateToAccount:
    def test_navigate_to_personal_account_after_login(self, driver):
        driver.get(data.Urls.login_page)
        driver.find_element(By.XPATH, locators.email).send_keys(data.UserCredits.email)
        driver.find_element(By.XPATH, locators.password).send_keys(data.UserCredits.password)
        driver.find_element(By.XPATH, locators.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.bread_tab)))
        driver.find_element(By.XPATH, locators.to_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.orders_history)))
        assert driver.find_element(By.CSS_SELECTOR, "a[href='/account/profile']").is_displayed()
