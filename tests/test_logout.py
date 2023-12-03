from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data_for_test


def test_logout_after_login():
    driver = webdriver.Chrome()
    driver.get(data_for_test.login_page_url)
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(data_for_test.user_email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(data_for_test.user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))

    driver.find_element(By.XPATH, ".//header/nav/a").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="История заказов"]')))

    driver.find_element(By.XPATH, './/button[text()="Выход"]').click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'Auth_link__1fOlj')))

    assert driver.find_element(By.XPATH, ".//button[text()='Войти']").is_displayed()
    driver.quit()

