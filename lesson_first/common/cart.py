from ..common.page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(BasePage):

    def find_elem(self, path):
        btn_item_elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(path))
        return btn_item_elem

