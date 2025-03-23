from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class TodayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATION = (By.CSS_SELECTOR, "#MainContent [data-testid='CurrentConditionsContainer'] .CurrentConditions--location--yub4l")
    DETAILS_LOCATION = (By.CSS_SELECTOR, "#todayDetails [data-testid='HeaderTitle']")
    TODAY_LINK = (By.CSS_SELECTOR, "#TimeFrameTabList-tab_0")
    HOURLY_LINK = (By.CSS_SELECTOR, "TimeFrameTabList-tab_1")
    DAILY_LINK = (By.CSS_SELECTOR, "TimeFrameTabList-tab_2")
    WEATHER_TABLE = (By.CSS_SELECTOR, "[data-testid='WeatherTable']")
    TEMPERATURE_VALUE = (By.CSS_SELECTOR, "[data-testid='SegmentHighTemp']")
    TIME_OF_DAY = (By.CSS_SELECTOR, ".Ellipsis--ellipsis--zynqj")
    TODAY_DETAILS = (By.CSS_SELECTOR, "div[class^='TodayDetailsCard--detailsContainer'")
    WEATHER_DETAILS_LIST_ITEM = (By.CSS_SELECTOR, "[data-testid='WeatherDetailsListItem']")
    WETAHER_DETAILS_LABEL = (By.CSS_SELECTOR, "pip install geopy")



