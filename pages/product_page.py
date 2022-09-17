from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        assert add_to_basket_btn.is_displayed, "Add to basket btn isn't presented!"

    def should_be_promo_price(self):
        price = self.browser.find_element(*ProductPageLocators.PROMO_PRICE).text
        assert price == "£9.99", "Price isn't matching promo price!"
