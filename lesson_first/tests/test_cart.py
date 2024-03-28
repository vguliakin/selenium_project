import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from ..tests.fixtures import *
from ..common.constants import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..common.auth import LoginPage
from ..common.cart import CatalogPage


def check_title_item(wait, path, title):
    title_cart_elems = wait.until(EC.presence_of_all_elements_located(path))

    flag = False

    for item in title_cart_elems:
        if item.text == title:
            flag = True

    return flag


@pytest.mark.success
def test_adding_item_to_cart(firefox_driver, login):
    login.enter_username(login.USR_FIELD, 'standard_user')
    login.enter_password(login.PASS_FIELD, 'secret_sauce')
    login.click_login(LOGIN_BTN)

    firefox_driver.maximize_window()
    wait = WebDriverWait(firefox_driver, 10)

    btn_item_elem = wait.until(EC.element_to_be_clickable(BTN_ADD_TO_CART))
    title_item_elem = btn_item_elem.find_element(*TITLE_ITEM_ELEM).text
    btn_item_elem.click()

    btn_cart_elem = wait.until(EC.element_to_be_clickable(BTN_CART))
    btn_cart_elem.click()

    __is_cart = firefox_driver.current_url == "https://www.saucedemo.com/cart.html"

    if not __is_cart:
        assert False

    assert check_title_item(wait, TITLE_CART_PRODUCT, title_item_elem)

@pytest.mark.success
def test_deleting_item_from_cart(firefox_driver, auth):

    catalog_page = CatalogPage(firefox_driver)

    item_title = catalog_page.find_elem(ITEM_CARD_TITLE).text

    item_btn_add = catalog_page.find_elem(ITEM_BTN_ADD)
    item_btn_add.click()

    cart = catalog_page.find_elem(BTN_CART)
    cart.click()

    btn_remove = catalog_page.find_elem((By.XPATH, f"//button[@id='remove-{item_title.lower().replace(' ', '-')}']"))
    btn_remove.click()

    try:
        firefox_driver.find_element(By.XPATH, f"//div[text()='{item_title}']")
    except selenium.common.exceptions.NoSuchElementException:
        assert True
    else:
        assert False


@pytest.mark.success
def test_add_item_from_card(firefox_driver, auth):

    catalog_page = CatalogPage(firefox_driver)

    item_card = catalog_page.find_elem((By.XPATH, "(//div[@class='inventory_item_img']/a)[1]"))
    item_card.click()

    card_btn_add = catalog_page.find_elem((By.XPATH, "//button[@id='add-to-cart']"))
    item_title = catalog_page.find_elem((By.XPATH, "//div[@class='inventory_details_name large_size']")).text
    card_btn_add.click()

    catalog_page.find_elem(BTN_CART).click()

    assert check_title_item(WebDriverWait(firefox_driver,10), TITLE_CART_PRODUCT, item_title)

@pytest.mark.success
def test_deleting_item_from_card(firefox_driver, auth):

    catalog_page = CatalogPage(firefox_driver)

    catalog_page.find_elem((By.XPATH, "(//div[@class='inventory_item_img']/a)[1]")).click()

    catalog_page.find_elem((By.XPATH, "//button[@id='add-to-cart']")).click()

    catalog_page.find_elem((By.XPATH, "//button[@id='remove']")).click()

    try:
        btn_del_from_card = firefox_driver.find_element(By.ID, "remove")
    except NoSuchElementException:
        assert True
    else:
        assert False


