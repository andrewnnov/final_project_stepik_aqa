import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_description()
        self.should_be_product_information_table()
        self.should_be_add_to_basket_button()



    def should_be_product_description(self):

        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Product description is not presented"


    def should_be_product_information_table(self):

        assert self.is_element_present(*ProductPageLocators.PRODUCT_INFORMATION), \
            "Product information table is not presented"


    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), \
            "Add to basket button is not presented"


    def should_be_add_to_basket_button_current_product(self):
        current_product = self.browser.find_element(*ProductPageLocators.CURRENT_PRODUCT)
        name_of_product = current_product.text
        print("Name of product: " + name_of_product)
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_CURRENT_PRODUCT).text
        print("Name of added product: " + added_product)
        assert name_of_product == added_product, "Current product in not in basket"


    def should_be_price_current_product_equal_added_product(self):
        price_current_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_CURRENT_PRODUCT)
        price_current_product_text = price_current_product.text
        print("Name of product: " + price_current_product_text)
        added_product_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_ADDED_PRODUCT).text
        print("Name of added product: " + added_product_price)
        assert price_current_product_text == added_product_price, "Current price in not equal price in basket"



    def click_to_add_to_basket_button(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_btn.click()






