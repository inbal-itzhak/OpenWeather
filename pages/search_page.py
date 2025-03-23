import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    SEARCH_BAR = (By.CSS_SELECTOR, "#LocationSearch_input")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-testid='ctaButton']")
    LANGUAGE_SELECTOR = (By.CSS_SELECTOR, "[data-testid='languageSelectorStatus']")
    LOCATION_LIST = (By.CSS_SELECTOR, "#LocationSearch_listbox")

    def find_first_search_result(self, city):
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.click()
        search_bar.clear()
        self.driver.find_element(*self.LANGUAGE_SELECTOR).click()
        search_bar.send_keys(city)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.LOCATION_LIST))
        search_results = self.driver.find_elements(*self.SEARCH_RESULTS)
        print(f"search results number is {len(search_results)}")
        if len(search_results) > 0:
            for search_result in search_results:
                search_result.click()
                break

