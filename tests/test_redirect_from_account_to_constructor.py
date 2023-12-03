from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data


class TestRedirectToConstructor:

    @staticmethod
    def login_helper(driver):
        driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys(data.UserCredits.email)
        driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(data.UserCredits.password)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    def test_redirect_due_to_constructor_button(self, driver):
        driver.get(data.Urls.login_page)
        TestRedirectToConstructor.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        driver.find_element(By.XPATH, ".//*[@href='/account']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="История заказов"]')))
        driver.find_element(By.XPATH, './/p[text()="Конструктор"]').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.button_button__33qZ0')))
        assert driver.find_element(By.CSS_SELECTOR, "ul.BurgerConstructor_basket__list__l9dp_").is_displayed()


    def test_redirect_due_to_logo_button(self, driver):
        driver.get(data.Urls.login_page)
        TestRedirectToConstructor.login_helper(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        driver.find_element(By.XPATH, ".//*[@href='/account']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="История заказов"]')))
        driver.find_element(By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.button_button__33qZ0')))
        assert driver.find_element(By.CSS_SELECTOR, "ul.BurgerConstructor_basket__list__l9dp_").is_displayed()
