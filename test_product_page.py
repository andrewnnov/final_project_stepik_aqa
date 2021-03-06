import time

import pytest

from .pages.login_page import LoginPage
from .pages.main_page import BasePage, MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

list_of_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = "QwertY1234567@"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(10)
        page.click_to_add_to_basket_button()
        base_page = BasePage(browser, link)
        base_page.solve_quiz_and_get_code()

        page.should_be_add_to_basket_button_current_product()
        page.should_be_price_current_product_equal_added_product()


@pytest.mark.need_review
@pytest.mark.parametrize(
    "link",
    [
        (list_of_number[0]),
        (list_of_number[1]),
        (list_of_number[2]),
        (list_of_number[3]),
        (list_of_number[4]),
        (list_of_number[5]),
        (list_of_number[6]),
        pytest.param(list_of_number[7], marks=pytest.mark.xfail(reason="some bug")),
        (list_of_number[8]),
        (list_of_number[9])
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.click_to_add_to_basket_button()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()

    page.should_be_add_to_basket_button_current_product()
    page.should_be_price_current_product_equal_added_product()



@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_basket_button()
    page.should_be_element_is_disappeared_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_header()
    basket_page.should_not_be_button_proceed_if_empty()
