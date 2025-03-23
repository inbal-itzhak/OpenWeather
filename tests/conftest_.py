import pytest
from selenium import webdriver
from pages.monthly_page import MonthlyPage
from pages.radar_page import RadarPage
from pages.ten_days_page import TenDaysPage
from pages.today_page import TodayPage
from pages.weekend_page import WeekendPage


@pytest.fixture(scope="class", autouse=True)
def setup_driver_class(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.today_page = TodayPage(request.cls.driver)
    request.cls.ten_days = TenDaysPage(request.cls.driver)
    request.cls.month_page = MonthlyPage(request.cls.driver)
    request.cls.weekend_page = WeekendPage(request.cls.driver)
    request.cls.radar_page = RadarPage(request.cls.driver)
    yield
    request.cls.driver.quit()


