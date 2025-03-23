from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    basu_url = "https://weather.com/"
    def __init__(self, driver):
        self.driver: WebDriver = driver
