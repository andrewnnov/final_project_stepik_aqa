from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    # LOGIN_EMAIL = (By.ID, "id_login-username")
    # LOGIN_PASSWORD = (By.ID, "id_login-password")
    # LOGIN_BUTTON = (By.XPATH, "//button[@name='login_submit']")
    #
    # REGISTER_EMAIL = (By.ID, "id_registration-email")
    # REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    # REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

