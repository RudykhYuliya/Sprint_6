import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 900)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
