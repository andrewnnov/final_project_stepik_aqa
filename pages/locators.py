from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    BTN_REGISTER_USER = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PRODUCT_DESCRIPTION = (By.XPATH, "//div[@id='product_description']/h2")
    PRODUCT_REVIEWS = (By.XPATH, "//div[@id='reviews']/h2")
    PRODUCT_INFORMATION = (By.XPATH, "//table[@class='table table-striped']")
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//form[@id='add_to_basket_form']//button")
    CURRENT_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    ADDED_CURRENT_PRODUCT = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRICE_OF_CURRENT_PRODUCT =(By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRICE_OF_ADDED_PRODUCT = (By.XPATH, "//div[@class='alertinner ']/p/strong")


class BasketPageLocators():
    BASKET_HEADER = (By.XPATH, "//div[@class='page-header action']/h1")
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']")
    BASKET_PROCEED_TO_CHECKOUT = (By.XPATH, "//div[@class='form-group clearfix']//div/a")


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

