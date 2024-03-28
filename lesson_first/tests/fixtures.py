import pytest
from ..common.constants import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..common.auth import LoginPage



@pytest.fixture()
def firefox_driver():
    driver = webdriver.Firefox()

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def login(firefox_driver):
    login_page = LoginPage(firefox_driver)
    login_page.open_page(BASE_URL)
    firefox_driver.implicitly_wait(10)
    yield login_page

@pytest.fixture()
def auth(login):
    login.enter_username(login.USR_FIELD, 'standard_user')
    login.enter_password(login.PASS_FIELD, 'secret_sauce')

    login.click_login(LOGIN_BTN)

@pytest.fixture()
def add_item_to_cart(firefox_driver):
    wait = WebDriverWait(firefox_driver, 10)
    btn_item_elem = wait.until(EC.element_to_be_clickable(BTN_ADD_TO_CART))
    btn_item_elem.click()

    btn_cart_elem = wait.until(EC.element_to_be_clickable(BTN_CART))
    btn_cart_elem.click()
