import pytest

from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('param', ['?promo=offer0',
                                   '?promo=offer1',
                                   '?promo=offer2',
                                   '?promo=offer3',
                                   '?promo=offer4',
                                   '?promo=offer5',
                                   '?promo=offer6',
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail),                                   '?promo=offer8',
                                   '?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, param):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{param}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.add_to_cart_message()
    page.cart_value_message()
    #time.sleep(10)
