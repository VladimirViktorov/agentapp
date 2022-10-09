from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.constant import URL
import pytest

def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, URL.LOGIN_PAGE_URL)
    page.open()
    page.should_be_login_page()

def test_guest_can_go_to_password_recovery_page(browser):
    page = LoginPage(browser, URL.LOGIN_PAGE_URL)
    page.open()
    page.go_to_password_recovery_page()
    login_page = PasswordRecoveryPage(browser, browser.current_url)
    login_page.should_be_password_recovery_page()

def test_do_not_enter_email(browser):
    page = LoginPage(browser, URL.LOGIN_PAGE_URL)
    page.open()
    page.do_not_enter_email()

@pytest.mark.parametrize('email', [pytest.param("@mail.ru", marks=pytest.mark.xfail),
                                  f"{'m'*81}@mail.ru",
                                  pytest.param("mail@.ru", marks=pytest.mark.xfail),
                                  f"mail@{'m'*81}.ru",
                                  "mail@mail.",
                                  "mail@mail.r",
                                  f"mail@mail.{'r'*21}"])
def test_enter_wrong_email_format(browser, email):
    page = LoginPage(browser, URL.LOGIN_PAGE_URL)
    page.open()
    page.enter_wrong_email_format(email)

@pytest.mark.parametrize('email', ["m@mail.ru", 
                                  f"{'m'*80}@mail.ru",
                                  "mail@m.ru",
                                  f"mail@{'m'*80}.ru",
                                  "mail@mail.ru",
                                  f"mail@mail.{'r'*20}"])
def test_enter_valid_email_format(browser, email):
    page = LoginPage(browser, URL.LOGIN_PAGE_URL)
    page.open()
    page.enter_valid_email_format(email)

