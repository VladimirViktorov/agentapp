from pages.login_page import LoginPage
from pages.constant import LOGIN_PAGE_URL

def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, LOGIN_PAGE_URL)
    page.open()
    page.should_be_login_page()