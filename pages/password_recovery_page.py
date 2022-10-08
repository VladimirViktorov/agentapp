from pages.base_page import BasePage
from pages.constant import URL
from pages.locators import PasswordRecoveryPageLocators

class PasswordRecoveryPage(BasePage):
    
    def should_be_password_recovery_page(self):
        self.should_be_password_recovery_url()
        self.should_be_login_input()
        self.should_be_password_input()
        self.should_be_repeat_password_input()
        self.should_be_send_button()
        self.should_be_enter_button()
        self.should_not_be_repeat_button()
        self.should_not_be_verification_code_input()
    
    def should_be_password_recovery_url(self):
        login_url = self.browser.current_url
        assert login_url == URL.PASSWORD_RECOVERY_PAGE_URL, \
            f"Password recovery url is not True. URL: '{login_url}'"
    
    def should_be_login_input(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.LOGIN_INPUT), \
            "Login input is not presented"
    
    def should_be_password_input(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.PASSWORD_INPUT), \
            "Password input is not presented"
    
    def should_be_repeat_password_input(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.REPEAT_PASSWORD_INPUT), \
            "Repeat password input is not presented"
    
    def should_be_send_button(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.SEND_BUTTON), \
            "Send button is not presented"
    
    def should_be_enter_button(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.LOGIN_LINK), \
            "Enter button is not presented"
    
    def should_not_be_repeat_button(self):
        assert self.is_not_element_present(*PasswordRecoveryPageLocators.REPEAT_BUTTON), \
            "Repeat button is presented, but should not be"
    
    def should_not_be_verification_code_input(self):
        assert self.is_not_element_present(*PasswordRecoveryPageLocators.VERIFICATION_CODE_INPUT), \
            "Verification code input is presented, but should not be"
    
    def go_to_login_page(self):
        link = self.browser.find_element(*PasswordRecoveryPageLocators.LOGIN_LINK)
        link.click()