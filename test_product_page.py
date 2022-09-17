from .pages.product_page import ProductPage

link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    page.solve_quiz_and_get_code()


def test_guest_should_see_basket_btn(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()


def test_guest_should_have_promo_price(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_price()

