from ..src.page import BasePage


class LoginPage(BasePage):

    def enter_username(self, elem, username):
        self.driver.find_element(*elem).send_keys(username)

    def enter_password(self, elem, password):
        self.driver.find_element(*elem).send_keys(password)

    def click_login(self, elem):
        self.driver.find_element(*elem).click()

    def verify_successful_login(self, url):
        return self.driver.current_url == url