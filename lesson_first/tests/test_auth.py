import time
import pytest
from ..tests.fixtures import *
from ..common.constants import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..common.auth import LoginPage
from ..common.cart import CatalogPage



def test_auth_with_correct_data(firefox_driver, login):
    login.enter_username(login.USR_FIELD, 'standard_user')
    login.enter_password(login.PASS_FIELD, 'secret_sauce')

    login.click_login(LOGIN_BTN)

    assert login.verify_successful_login(SECOND_URL)


def test_auth_with_wrong_data(firefox_driver, login):
    login.enter_username(login.USR_FIELD, 'standard')
    login.enter_password(login.PASS_FIELD, 'secret')

    login.click_login(LOGIN_BTN)

    assert not (login.verify_successful_login(SECOND_URL))





