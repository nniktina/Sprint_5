from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data_for_test


def test_navigate_to_personal_account_after_login():
    driver = webdriver.Chrome()
    driver.get(data_for_test.login_page_url)
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(data_for_test.user_email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(data_for_test.user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Булки"]')))
    driver.find_element(By.XPATH, ".//header/nav/a").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="История заказов"]')))
    assert driver.current_url == data_for_test.profile_url
    driver.quit()

