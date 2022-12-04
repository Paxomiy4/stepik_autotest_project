from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
import math


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), "Product is presented, but should not be"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
