from pages.base_page import BasePage
from pages.constant import ENTER_PAGE_URL
from pages.locators import EnterPageLocators

class EnterPage(BasePage):
    
    def should_be_enter_page(self):
        self.should_be_enter_url()
        self.should_be_record_preview()
        self.should_be_record_alarm()
        self.should_be_record_forgot_password()
        self.should_be_record_forgot_login()
        self.should_be_record_memo()
        self.should_be_record_team()
        self.should_be_record_schedule()
        self.should_be_record_promo()
        self.should_be_record_need_help()
    
    def should_be_enter_url(self):
        enter_url = self.browser.current_url
        assert enter_url == ENTER_PAGE_URL, \
            f"Enter url is not True. URL: '{enter_url}'"
    
    def should_be_record_preview(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_PREVIEW), \
            "Record preview is not presented"
    
    def should_be_record_alarm(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_ALARM), \
            "Record alarm is not presented"
    
    def should_be_record_forgot_password(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_FORGOT_PASSWORD), \
            "Record forgot password is not presented"
    
    def should_be_record_forgot_login(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_FORGOT_LOGIN), \
            "Record forgot login is not presented"
    
    def should_be_record_memo(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_MEMO), \
            "Record memo is not presented"
    
    def should_be_record_team(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_TEAM), \
            "Record team is not presented"
    
    def should_be_record_schedule(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_SCHEDULE), \
            "Record schedule is not presented"
    
    def should_be_record_promo(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_PROMO), \
            "Record promo is not presented"
    
    def should_be_record_need_help(self):
        assert self.is_element_present(*EnterPageLocators.RECORD_NEED_HELP), \
            "Record need help is not presented"