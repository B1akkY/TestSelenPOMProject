from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_basket_is_empty()
        self.should_be_basket_is_empty_notification()

    def should_be_basket_is_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BUY_BTN)

    def should_be_basket_is_empty_notification(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_NOTIFICATION)
