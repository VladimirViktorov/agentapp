from pages.base_page import BasePage
from pages.constant import URL, TEXT
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_container_login_form()
        self.should_be_container_information()
        self.should_be_login_input()
        self.should_be_password_input()
        self.should_be_enter_button()
        self.should_be_forgot_password_button()
    
    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url == URL.LOGIN_PAGE_URL, \
            f"Login url is not True. URL: '{login_url}'"
    
    def should_be_container_login_form(self):
        assert self.is_element_present(*LoginPageLocators.CONTAINER_LOGINFORM), \
            "Container login form is not presented"
        
    def should_be_container_information(self):
        assert self.is_element_present(*LoginPageLocators.CONTAINER_INFORMATION), \
            "Container information is not presented"
    
    def should_be_login_input(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT), \
            "Login input is not presented"
    
    def should_be_password_input(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), \
            "Password input is not presented"
    
    def should_be_enter_button(self):
        assert self.is_element_present(*LoginPageLocators.ENTER_BUTTON), \
            "Enter button is not presented"
    
    def should_be_forgot_password_button(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RECOVERY_LINK), \
            "Forgot password button is not presented"
    
    def go_to_password_recovery_page(self):
        link = self.browser.find_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK)
        link.click()
    
    def should_be_login_error_message(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_ERROR_MESSAGE), \
            "Login error message is not presented"
    
    def do_not_enter_email(self):
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_input.click()
        self.should_be_login_error_message()
        error_message = self.browser.find_element(*LoginPageLocators.LOGIN_ERROR_MESSAGE).text
        assert error_message == TEXT.ERROR_MESSAGE_DO_NOT_ENTER_EMAIL, f"Wrong error message. Received message: '{error_message}'"
    
    def enter_wrong_email_format(self, email):
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_input.send_keys(email)
        self.should_be_login_error_message()
        error_message = self.browser.find_element(*LoginPageLocators.LOGIN_ERROR_MESSAGE).text
        assert error_message == TEXT.ERROR_MESSAGE_ENTER_WRONG_FORMAT, f"Wrong error message. Received message: '{error_message}'"
    
    def enter_valid_email_format(self, email):
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_input.send_keys(email)
        assert self.is_not_element_present(*LoginPageLocators.LOGIN_ERROR_MESSAGE), \
            "Login error message is presented, but should not be"
        