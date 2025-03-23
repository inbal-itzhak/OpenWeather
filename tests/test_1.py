import time

from selenium import webdriver
from selenium.webdriver import chrome
from pages.radar_page import RadarPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.today_page import TodayPage
from pages.search_page import SearchPage
import pytest


class TestWeather:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://weather.com/")
        print(f"Driver initialized: {driver}")
        tp = TodayPage(driver)
        sp = SearchPage(driver)
        rp = RadarPage(driver)
        actions = ActionChains(driver)
        yield driver, tp, sp, rp, actions
        driver.quit()

    def test1(self, setup):
        driver, tp, sp, rp, actions = setup
        assert driver is not None, "Driver is not initialized"
        city = "Rosh HaAyin"
        sp.find_first_search_result(city)
        time.sleep(5)
        rp.wait_for_map()
        X, Y = rp.get_coordinates()
        city_name = rp.get_map_city_name(X, Y)
        print(f"city name = {city_name}, X = {X}, Y = {Y}")
