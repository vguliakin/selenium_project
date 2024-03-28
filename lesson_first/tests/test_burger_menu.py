import time

import pytest

from ..tests.fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def test_logout(firefox_driver, auth):

    firefox_driver.maximize_window()

    action = ActionChains(firefox_driver)
    burger_menu = firefox_driver.find_element(By.ID, 'react-burger-menu-btn')
    logout_btn = firefox_driver.find_element(By.ID, 'logout_sidebar_link')

    action.move_to_element(burger_menu).click(burger_menu).perform()

    firefox_driver.implicitly_wait(10)

    action.move_to_element(logout_btn).click(logout_btn).perform()

    assert firefox_driver.current_url == "https://www.saucedemo.com/"

    if not firefox_driver.get_cookies():
        assert True
    else:
        assert False

def test_redirection_to_about(firefox_driver, auth):
    firefox_driver.maximize_window()

    action = ActionChains(firefox_driver)
    burger_menu = firefox_driver.find_element(By.ID, 'react-burger-menu-btn')
    about_btn = firefox_driver.find_element(By.ID, 'about_sidebar_link')

    action.move_to_element(burger_menu).click(burger_menu).perform()
    firefox_driver.implicitly_wait(100)
    action.move_to_element(about_btn).click(about_btn).perform()

    time.sleep(5)

    assert firefox_driver.current_url == "https://saucelabs.com/"

def test_reset_app_state(firefox_driver, auth, add_item_to_cart):

    action = ActionChains(firefox_driver)
    burger_menu = firefox_driver.find_element(By.ID, 'react-burger-menu-btn')
    reset_btn = firefox_driver.find_element(By.ID, 'reset_sidebar_link')

    action.move_to_element(burger_menu).click(burger_menu).perform()
    action.move_to_element(reset_btn).click(reset_btn).perform()

    storage = firefox_driver.execute_script("return localStorage.getItem('cart-contents')")

    assert True if storage is None else False

