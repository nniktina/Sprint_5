from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import data_for_test


def test_correct_data_successful_registration(username, correct_password, user_email):
    driver = webdriver.Chrome()
    driver.get(data_for_test.reg_url_page)

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(username)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(user_email)
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(correct_password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    assert driver.current_url == data_for_test.login_page_url
    driver.quit()


def test_wrong_password_failed_registration(username, incorrect_password, user_email):
    driver = webdriver.Chrome()
    driver.get(data_for_test.reg_url_page)

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(username)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(user_email)
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(incorrect_password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.input__error')))
    assert driver.find_element(By.CSS_SELECTOR, '.input__error').text == "Некорректный пароль"
    driver.quit()