from selenium.webdriver.common.by import By

SECOND_URL = "https://www.saucedemo.com/inventory.html"
LOGIN_BTN = (By.ID, 'login-button')
BASE_URL = "https://www.saucedemo.com/"

BTN_ADD_TO_CART = (By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory '])[1]")
BTN_CART = (By.XPATH, "//a[@class='shopping_cart_link']")
TITLE_CART_PRODUCT = (By.XPATH, "//div[@class='inventory_item_name']")
TITLE_ITEM_ELEM = (By.XPATH, "../parent::div/parent::div//div[@class='inventory_item_name ']")
LOGIN_BTN = (By.ID, 'login-button')

ITEM_CARD = (By.XPATH, "(//div[@class='inventory_item_description'])[1]")
ITEM_CARD_TITLE = (By.XPATH, ITEM_CARD[1] + "//div[@class='inventory_item_name ']")
ITEM_BTN_ADD = (By.XPATH, ITEM_CARD[1] + "//button")