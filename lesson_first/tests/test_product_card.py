import pytest

from ..tests.fixtures import *
from selenium.webdriver.common.by import By

ID_ITEM = 4
URL_CARD = f"https://www.saucedemo.com/inventory-item.html?id={ID_ITEM}"

@pytest.mark.success
def test_redirection_by_img(firefox_driver, auth):

    firefox_driver.find_element(By.ID, f'item_{ID_ITEM}_img_link').click()

    assert firefox_driver.current_url == URL_CARD

@pytest.mark.success
def test_redirection_by_title(firefox_driver, auth):

    title_link = firefox_driver.find_element(By.ID, f'item_{ID_ITEM}_title_link')

    firefox_driver.execute_script("arguments[0].click();", title_link)

    assert firefox_driver.current_url == URL_CARD