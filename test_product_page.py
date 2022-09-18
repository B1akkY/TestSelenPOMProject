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
def test_guest_can_add_product_to_basket(browser, link):
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



@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207",
    "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
