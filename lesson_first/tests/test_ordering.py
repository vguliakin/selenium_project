import pytest

from ..tests.fixtures import *
from selenium.webdriver.common.by import By


def test_ordering_with_right_credentials(firefox_driver, auth, add_item_to_cart):

    __url_step_one = "https://www.saucedemo.com/checkout-step-one.html"
    __url_step_two = "https://www.saucedemo.com/checkout-step-two.html"
    __url_complete = "https://www.saucedemo.com/checkout-complete.html"

    __first_name = "Nika"
    __last_name = "Abramov"
    __postcode = 11333

    firefox_driver.find_element(By.ID, 'checkout').click()

    assert firefox_driver.current_url == __url_step_one

    firefox_driver.find_element(By.ID, 'first-name').send_keys(__first_name)
    firefox_driver.find_element(By.ID, 'last-name').send_keys(__last_name)
    firefox_driver.find_element(By.ID, 'postal-code').send_keys(__postcode)

    firefox_driver.find_element(By.ID, 'continue').click()

    assert firefox_driver.current_url == __url_step_two

    firefox_driver.find_element(By.ID, 'finish').click()

    assert firefox_driver.current_url == __url_complete

