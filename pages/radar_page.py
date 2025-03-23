from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from geopy.geocoders import Nominatim
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MAP_ELEMENT = (By.CSS_SELECTOR, "div[class^='Slideshow']")
    LOCATION_PIN = (By.CSS_SELECTOR, "[data-testid='LocationPin']")

    def wait_for_map(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.MAP_ELEMENT))


    def get_coordinates(self):
        map_element = self.driver.find_element(*self.MAP_ELEMENT)
        map_size = map_element.size
        W, H = map_size['width'], map_size['height']
        location_pin = self.driver.find_element(*self.LOCATION_PIN)
        style = location_pin.get_attribute("style")
        print(f"Style attribute: {style}")
        left_match = re.search(r"left:\s*calc\(50%\s*-\s*(\d+)px\);", style)
        top_match = re.search(r"top:\s*calc\(\s*([\d.]+)%\s*-\s*(\d+)px\);", style)
        if left_match and top_match:
            left_offset = int(left_match.group(1))
            top_percent = float(top_match.group(1))
            top_offset = int(top_match.group(2))
            X = 0.5 * W - left_offset
            Y = (top_percent / 100) * H - top_offset
            print(f"LocationPin coordinates: ({X}, {Y}) in pixels")
            return X, Y
        else:
            print(f"Error: Could not parse style attribute. Left match: {left_match}, Top match: {top_match}")
            print(f"Style String: {style}")  # Print the style string for debugging
            return None, None  # Or raise an exception

    def get_map_city_name(self, lat, lon):
        geolocator = Nominatim(user_agent="geo_locator")
        location = geolocator.reverse((lat, lon), language="en")
        if location and "address" in location.raw:
            return location.raw["address"].get("city", "Unknown location")
        return "Unknown location"


