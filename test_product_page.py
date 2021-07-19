import time

from .pages.main_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.click_to_add_to_basket_button()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()

    page.should_be_add_to_basket_button_current_product()
    page.should_be_price_current_product_equal_added_product()




