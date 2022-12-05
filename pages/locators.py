from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div > h1")
    BOOK_NAME_ALERT = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "span > a")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")


class BasketPageLocators:
    PRODUCT = (By.CSS_SELECTOR, "div.basket-items > div")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div[id ='content_inner'] > p")
