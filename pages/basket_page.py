from .base_page import BasePage
from .locators import BasketPageLocators

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida",
    "cs": "Váš košík je prázdný",
    "da": "Din indkøbskurv er tom",
    "de": "Ihr Warenkorb ist leer",
    "en": "Your basket is empty",
    "el": "Το καλάθι σας είναι άδειο",
    "es": "Tu carrito esta vacío",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide",
    "it": "Il tuo carrello è vuoto",
    "ko": "장바구니가 비었습니다",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty",
    "pt": "O carrinho está vazio",
    "pt-br": "Sua cesta está vazia",
    "ro": "Cosul tau este gol",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий",
    "zh-cn": "Your basket is empty",
}


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_basket_is_empty()
        self.should_be_basket_is_empty_notification()

    def should_be_basket_is_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BUY_BTN), \
            "There is a product in the basket, although there should not be one"

    def should_be_basket_is_empty_notification(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_NOTIFICATION).text
        text_lst = text.split('.')
        empty_text = text_lst[0]
        assert empty_text in languages.values(), "There is no empty basket text presented"
