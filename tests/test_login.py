from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data_for_test


def test_login_from_main_page_successful():
    driver = webdriver.Chrome()
    driver.get(data_for_test.main_page_url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(data_for_test.user_email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(data_for_test.user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == data_for_test.main_page_url
    driver.quit()


def test_login_from_personal_account_button():
    driver = webdriver.Chrome()
    driver.get(data_for_test.main_page_url)
    driver.find_element(By.XPATH, ".//header/nav/a").click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(data_for_test.user_email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(data_for_test.user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == data_for_test.main_page_url
    driver.quit()


def test_login_from_registration_page():
    driver = webdriver.Chrome()
    driver.get(data_for_test.reg_url_page)
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(data_for_test.user_email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(data_for_test.user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == data_for_test.main_page_url
    driver.quit()


def test_login_from_password_forgot_page():
    driver = webdriver.Chrome()
    driver.get(data_for_test.forgot_url)
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(data_for_test.user_email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(data_for_test.user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == data_for_test.main_page_url
    driver.quit()