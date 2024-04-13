class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_button(self, elem):
        self.driver.find_element(*elem).click()

