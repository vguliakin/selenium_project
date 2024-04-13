import time
import pytest
from pages.product_page import ProductPage
from src.product_data import ProductData
from locators.product_locators import ProductLocators as PL
from src.urls import Urls


class TestProductPage:
    
    url_product_page = Urls.BASE_URL

    @pytest.mark.skip
    @pytest.mark.parametrize('promo_offer', ProductData.PROMO_OFFER)
    def test_add_to_cart_from_product_page(self, driver, promo_offer):
        page = ProductPage(driver, promo_offer)

        page.open()

        page.click_on_element(PL.ADD_TO_CART_BTN)
        page.solve_quiz_and_get_code()

        expected_text = page.get_text(PL.HEADER_OF_PRODUCT)

        actual_text = page.get_text(PL.TEXT_OF_PRODUCT)
        print(actual_text)

        assert actual_text == expected_text, f'The bug on the website - {page.driver.current_url}'

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/')

        page.open()

        page.click_on_element(PL.ADD_TO_CART_BTN)

        assert page.is_not_element_present(PL.SUCCESS_MSG)
    
    def test_guest_cant_see_success_message(self, driver):
        page = ProductPage(driver, 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/')

        page.open()

        assert page.is_not_element_present(PL.SUCCESS_MSG)

    def test_message_disappeared_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/')

        page.open()

        page.click_on_element(PL.ADD_TO_CART_BTN)

        assert page.is_disappeared(PL.SUCCESS_MSG)






