import time

import pytest

from ..tests.fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_items(items, correct_items):
    flag = True

    for i in range(len(items)):
        if not items[i].text == correct_items[i]:
            flag = False

    return flag

def change_filter_mode(firefox_driver, option, item):
    filter_menu = Select(firefox_driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    filter_menu.select_by_value(option)

    wait = WebDriverWait(firefox_driver, 10)
    items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, item)))

    return items

@pytest.mark.success
def test_filtering_by_name_a_to_z(firefox_driver, auth):

    items = change_filter_mode(firefox_driver, 'az', 'inventory_item_name ')
    a_to_z_items = list(map(lambda x: x.text, items))
    a_to_z_items.sort()

    assert check_items(items, a_to_z_items)

@pytest.mark.success
def test_filtering_by_name_z_to_a(firefox_driver, auth):

    items = change_filter_mode(firefox_driver, 'za', 'inventory_item_name ')
    z_to_a_items = list(map(lambda x: x.text, items))
    z_to_a_items.sort(reverse=True)

    assert check_items(items, z_to_a_items)

@pytest.mark.test
def test_filtering_by_price_low(firefox_driver, auth):

    items = change_filter_mode(firefox_driver,"lohi", 'inventory_item_price')
    correct_items = list(map(lambda x: float(x.text.lstrip("$")), items))
    sorted_items = sorted(correct_items)

    if correct_items == sorted_items:
        assert True
    else:
        assert False

@pytest.mark.success
def test_filtering_by_price_high(firefox_driver, auth):

    items = change_filter_mode(firefox_driver, 'hilo', 'inventory_item_price')
    correct_items = list(map(lambda x: float(x.text.lstrip("$")), items))
    sorted_items = sorted(correct_items, reverse=True)

    if correct_items == sorted_items:
        assert True
    else:
        assert False