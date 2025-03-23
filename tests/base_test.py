from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.monthly_page import MonthlyPage
from pages.radar_page import RadarPage
from pages.ten_days_page import TenDaysPage
from pages.today_page import TodayPage
from pages.weekend_page import WeekendPage

class BaseTest:
    today_page:TodayPage
    ten_days_page:TenDaysPage
    monthly_page:MonthlyPage
    weekend_page:WeekendPage
    radar_page:RadarPage

