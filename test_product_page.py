import time

import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.need_review
@pytest.mark.parametrize("promo", ["0", "1", "2", "3", "4", "5", "6",
                                   pytest.param(7, marks=pytest.mark.xfail(reason="some bug")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_added_equals_product_name()


@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_should_see_basket_btn(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()


@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_should_have_promo_price_equals_total_added(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.should_be_promo_price_equals_total()


@pytest.mark.xfail
@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    page.should_not_be_success_message()


@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    page.should_be_success_message_disappeared()


@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "123456Hello"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_be_product_name_added_equals_product_name()
