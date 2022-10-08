from pages.password_recovery_page import PasswordRecoveryPage
from pages.login_page import LoginPage
from pages.constant import PASSWORD_RECOVERY_PAGE_URL

def test_guest_can_go_to_password_recovery_page(browser):
    page = PasswordRecoveryPage(browser, PASSWORD_RECOVERY_PAGE_URL)
    page.open()
    page.should_be_password_recovery_page()
    
def test_guest_can_go_to_login_page(browser):
    page = PasswordRecoveryPage(browser, PASSWORD_RECOVERY_PAGE_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()