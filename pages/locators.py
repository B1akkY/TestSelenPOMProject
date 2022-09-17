from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PROMO_PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in p:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")