import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
class TestProductPage():
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()

    def test_guest_should_see_basket_btn(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_btn()

    def test_guest_should_have_promo_price_equals_total_added(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_be_promo_price_equals_total()

    def test_guest_should_have_expected_product_to_be_added_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_be_product_name_added_equals_product_name()
