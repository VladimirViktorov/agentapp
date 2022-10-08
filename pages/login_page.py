from pages.base_page import BasePage
from pages.constant import LOGIN_PAGE_URL
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
        assert login_url == LOGIN_PAGE_URL, \
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
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_BUTTON), \
            "Forgot password button is not presented"