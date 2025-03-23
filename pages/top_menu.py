from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TopMenu(BasePage):
    def __init__(self):
        super().__init__()