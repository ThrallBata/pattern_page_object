from .base_page import BasePage
from .locators import PageObjectLocators
from selenium.webdriver.common.by import By


class PageObject(BasePage):
    def add_to_basket(self):
        add_basket = self.browser.find_element(*PageObjectLocators.ADD_BASKET)
        add_basket.click()