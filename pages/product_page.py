from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

    def add_product_to_basket(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_BASKET_BUTTON)
        )
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_correct_product_name(self, product_name):
        message_name = self.browser.find_element(*self.SUCCESS_MESSAGE).text

        assert product_name == message_name, \
            f"Expected product name '{product_name}', but got '{message_name}'"

    def should_be_correct_product_price(self, product_price):
        basket_price = self.browser.find_element(*self.BASKET_PRICE).text

        assert product_price == basket_price, \
            f"Expected price '{product_price}', but got '{basket_price}'"