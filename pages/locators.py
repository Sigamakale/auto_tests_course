from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div strong')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    CART_VALUE_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner > p:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, 'span a.btn-default')


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, '#basket_formset')