from pages.enter_page import EnterPage
from pages.constant import ENTER_PAGE_URL

def test_guest_can_go_to_enter_page(browser):
    page = EnterPage(browser, ENTER_PAGE_URL)
    page.open()
    page.should_be_enter_page()