from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    PRODUCT_DESCRIPTION = (By.XPATH, "//div[@id='product_description']/h2")
    PRODUCT_REVIEWS = (By.XPATH, "//div[@id='reviews']/h2")
    PRODUCT_INFORMATION = (By.XPATH, "//table[@class='table table-striped']")
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//form[@id='add_to_basket_form']//button")
    CURRENT_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    ADDED_CURRENT_PRODUCT = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRICE_OF_CURRENT_PRODUCT =(By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRICE_OF_ADDED_PRODUCT = (By.XPATH, "//div[@class='alertinner ']/p/strong")

