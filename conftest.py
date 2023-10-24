# file with fixtures used in tests

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Links
from tests.test_data import TestData
from pages.start_page import StartPage


@pytest.fixture(autouse=True)
def browser():
    """fixture to open Chrome browser before running tests, and to quit browser after that;
    automatically & implicitly started (by "autouse" parameter)
    for every test where this fixture is mentioned as a parameter of test"""
    service = Service("chromedriver")
    browser = webdriver.Chrome(service=service)

    yield browser

    browser.quit()


@pytest.fixture()
def msk_login(browser):
    """fixture to log in as a user registered with MSK phone number;
    starts from opening start page and finishes on My orders page"""
    start_page = StartPage(browser, Links.start_page)
    start_page.open_page()
    start_page.login(TestData.valid_login_credentials_msk_user[0])


@pytest.fixture()
def spb_login(browser):
    """fixture to login in as a user registered with SPB phone number;
    starts from opening start page and finishes on My orders page"""
    start_page = StartPage(browser, Links.start_page)
    start_page.open_page()
    start_page.login(TestData.valid_login_credentials_spb_user[0])

# ...