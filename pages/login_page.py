from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Should be on a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form should be presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form should be presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_field2.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit_button.click()
