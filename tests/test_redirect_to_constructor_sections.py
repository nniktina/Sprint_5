from selenium.webdriver.common.by import By
from selenium import webdriver
import data_for_test


def test_redirect_to_sauces_tab():
    driver = webdriver.Chrome()
    driver.get(data_for_test.main_page_url)
    driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
    tab_sauces = driver.find_element(By.XPATH, './/div/main/section[1]/div[1]/div[2]')
    sauces_classes = tab_sauces.get_attribute('class')
    assert 'tab_tab_type_current__2BEPc' in sauces_classes


def test_redirect_to_fillings_tab():
    driver = webdriver.Chrome()
    driver.get(data_for_test.main_page_url)
    driver.find_element(By.XPATH, './/span[text()="Начинки"]').click()
    tab_fillings = driver.find_element(By.XPATH, './/div/main/section[1]/div[1]/div[3]')
    filling_classes = tab_fillings.get_attribute('class')
    print(filling_classes)
    assert 'tab_tab_type_current__2BEPc' in filling_classes
    driver.quit()


def test_redirect_to_breads_tab():
    driver = webdriver.Chrome()
    driver.get(data_for_test.main_page_url)
    driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
    driver.find_element(By.XPATH, './/span[text()="Булки"]').click()
    tab_bread = driver.find_element(By.XPATH, './/div/main/section[1]/div[1]/div[1]')
    bread_classes = tab_bread.get_attribute('class')
    print(bread_classes)
    assert 'tab_tab_type_current__2BEPc' in bread_classes
    driver.quit()


