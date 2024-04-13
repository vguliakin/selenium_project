

class ProductLocators:
    
    ADD_TO_CART_BTN = ("css selector", "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    TEXT_OF_PRODUCT = ("xpath", "(//div[@class='alertinner ']/strong)[1]")
    HEADER_OF_PRODUCT = ("xpath", "//div[@class='col-sm-6 product_main']/h1")
    SUCCESS_MSG = ("xpath", "(//div[@id='messages']/div)[1]")