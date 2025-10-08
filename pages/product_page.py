from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        #add = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_btn.click()

    def add_to_cart_message(self):
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE)
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        assert name_of_product.text in message.text, f'Name of product in the message "{message.text}" does not match the one added to the cart "{name_of_product.text}".'

    def cart_value_message(self):
        message = self.browser.find_element(*ProductPageLocators.CART_VALUE_MESSAGE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text in message.text, f'Cart value in the message "{message.text}" does not match the one added to the cart "{product_price.text}".'

