from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):


    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()


    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        substring = 'basket'
        assert substring in self.browser.current_url, f"Substring {substring} is not present in current url"


    def should_be_basket_header(self):
        # реализуйте проверку, что есть header Basket
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), "Basket header is not presented"


    def should_not_be_button_proceed_if_empty(self):
        # проверка, что нет кнопки PROCEED_TO_CHECKOUT
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PROCEED_TO_CHECKOUT), "Basket is not empty"


