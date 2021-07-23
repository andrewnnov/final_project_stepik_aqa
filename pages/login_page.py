from .base_page import BasePage
from .locators import LoginPageLocators




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        substring = 'login'
        assert substring in self.browser.current_url, f"Substring {substring} is not present in current url"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"


    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        user_email.send_keys(email)

        user_pass = self.browser.find_element(*LoginPageLocators.PASSWORD)
        user_pass.send_keys(password)

        user_pass_conf = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        user_pass_conf.send_keys(password)

        registration_btn = self.browser.find_element(*LoginPageLocators.BTN_REGISTER_USER)
        registration_btn.click()





