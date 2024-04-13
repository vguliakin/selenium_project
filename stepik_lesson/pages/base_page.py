from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    __timeout = 10

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
    
    def open(self):
        self.driver.get(self.url)
    
    def click_on_element(self, locator):
        wait = WebDriverWait(self.driver, timeout=self.__timeout)
        e = wait.until(EC.element_to_be_clickable(locator))
        e.click()
    
    def get_text(self, locator):
        e = self.element_is_visible(locator)
        return e.text
    
    def element_is_visible(self, locator):
        wait = WebDriverWait(self.driver, timeout=self.__timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True
    

    