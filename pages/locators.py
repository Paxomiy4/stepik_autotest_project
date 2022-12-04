from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")