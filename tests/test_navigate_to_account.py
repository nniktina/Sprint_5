from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data


class TestNavigateToAccount:
    def test_navigate_to_personal_account_after_login(self, driver):
        driver.get(data.Urls.login_page)
        driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys(data.UserCredits.email)
        driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(data.UserCredits.password)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Булки"]')))
        driver.find_element(By.XPATH, ".//*[@href='/account']").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="История заказов"]')))
        assert driver.find_element(By.CSS_SELECTOR, "a[href='/account/profile']").is_displayed()
