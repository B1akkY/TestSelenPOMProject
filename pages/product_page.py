from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        assert add_to_basket_btn.is_displayed, "Add to basket button isn't presented!"

    def should_be_promo_price_equals_total(self):
        price = self.browser.find_element(*ProductPageLocators.PROMO_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert price == basket_total, "Price isn't matching total sum!"

    def should_be_product_name_added_equals_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_added = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text
        assert product_name == product_name_added, "Wrong product added to basket!"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message has not disappeared, but it should"
