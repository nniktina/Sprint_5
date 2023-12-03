from selenium.webdriver.common.by import By
import data


class TestSections:
    def test_redirect_to_sauces_tab(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
        tab_sauces = driver.find_element(By.XPATH, '//span[text()="Соусы"]/parent::div')
        sauces_classes = tab_sauces.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in sauces_classes


    def test_redirect_to_fillings_tab(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, './/span[text()="Начинки"]').click()
        tab_fillings = driver.find_element(By.XPATH, '//span[text()="Начинки"]/parent::div')
        filling_classes = tab_fillings.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in filling_classes


    def test_redirect_to_breads_tab(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
        driver.find_element(By.XPATH, './/span[text()="Булки"]').click()
        tab_bread = driver.find_element(By.XPATH, '//span[text()="Булки"]/parent::div')
        bread_classes = tab_bread.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in bread_classes


