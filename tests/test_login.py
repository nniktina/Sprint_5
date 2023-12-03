from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data


class TestLogin:

    @staticmethod
    def login_helper(driver):
        driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys(data.UserCredits.email)
        driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(data.UserCredits.password)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    def test_login_from_main_page_successful(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.find_element(By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7").is_displayed()

    def test_login_from_personal_account_button(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, ".//*[@href='/account']").click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.find_element(By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7").is_displayed()

    def test_login_from_registration_page(self, driver):
        driver.get(data.Urls.reg_page)
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.find_element(By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7").is_displayed()

    def test_login_from_password_forgot_page(self, driver):
        driver.get(data.Urls.forgot_pass)
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        TestLogin.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.find_element(By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7").is_displayed()