from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_REPEAT_PASSWORD)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email_input.send_keys(email)
        password_input.send_keys(password)
        repeat_password_input.send_keys(password)
        registration_button.click()

