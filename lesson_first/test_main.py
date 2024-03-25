import time
import pytest
from selenium import webdriver

BASE_URL = "https://www.saucedemo.com/"


def test_auth_verify():
    driver = webdriver.Firefox()

    driver.get(BASE_URL)
    driver.implicitly_wait(10)

    username_field = driver.find_element('xpath', "//input[@class='input_error form_input' and @data-test='username']")
    password_field = driver.find_element('xpath', "//input[@class='input_error form_input' and @data-test='password']")
    login_element = driver.find_element('xpath', "//input[@type='submit']")

    username_field.clear()
    username_field.send_keys("standard_user")

    assert username_field.text is not None

    time.sleep(1)
    password_field.clear()
    password_field.send_keys("secret_sauce")

    assert password_field.text is not None

    time.sleep(1)
    login_element.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()
