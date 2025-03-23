from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.today_page import TodayPage
import pytest

class TestGemini:
    @pytest.fixture(scope="class", autouse=True)  # autouse is often not recommended, see below
    def setup(self):
        driver = webdriver.Chrome()  # No self. here
        driver.maximize_window()
        driver.get("https://weather.com/")
        print(f"Driver initialized: {driver}")
        tp = TodayPage(driver)       # No self. here
        actions = ActionChains(driver) # No self. here
        yield driver, tp, actions      # Return the values as a tuple
        driver.quit() # very important to close the browser after the test is done

    def test1(self, setup):  # Note the 'setup' argument
        driver, tp, actions = setup  # Unpack the returned tuple

        assert driver is not None, "Driver is not initialized" # Use driver, not self.driver
        city = "Rosh HaAyin"
        search_bar = driver.find_element(*tp.SEARCH_BAR) # Use driver, not self.driver
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys(city)
        print(f"found search bar element {search_bar}")
        actions.send_keys_to_element(search_bar, Keys.RETURN) # Use actions
        map_element = driver.find_element(*tp.MAP_ELEMENT) # Use driver
        X, Y = tp.get_coordinates()
        city_name = tp.get_map_city_name(X, Y)
        print(f"city name = {city_name}, X = {X}, Y = {Y}")