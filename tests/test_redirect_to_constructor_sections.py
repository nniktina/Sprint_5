from selenium.webdriver.common.by import By
import data
import locators


class TestSections:
    def test_redirect_to_sauces_tab(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, locators.sauces_tab).click()
        tab_sauces = driver.find_element(By.XPATH, locators.sauces)
        sauces_classes = tab_sauces.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in sauces_classes


    def test_redirect_to_fillings_tab(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, locators.fills_tab).click()
        tab_fillings = driver.find_element(By.XPATH, locators.fills)
        filling_classes = tab_fillings.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in filling_classes


    def test_redirect_to_breads_tab(self, driver):
        driver.get(data.Urls.main_page)
        driver.find_element(By.XPATH, locators.sauces_tab).click()
        driver.find_element(By.XPATH, locators.bread_tab).click()
        tab_bread = driver.find_element(By.XPATH, locators.bread)
        bread_classes = tab_bread.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in bread_classes


