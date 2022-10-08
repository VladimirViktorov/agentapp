from pages.password_recovery_page import PasswordRecoveryPage
from pages.constant import PASSWORD_RECOVERY_PAGE_URL

def test_guest_can_go_to_password_recovery_page(browser):
    page = PasswordRecoveryPage(browser, PASSWORD_RECOVERY_PAGE_URL)
    page.open()
    page.should_be_password_recovery_page()