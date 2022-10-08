from selenium.webdriver.common.by import By

class BasePageLocators():
    pass

class LoginPageLocators():
    CONTAINER_LOGINFORM = (By.XPATH, "/html/body/app-root/app-login/div[1]")
    CONTAINER_INFORMATION = (By.XPATH, "/html/body/app-root/app-login/div[2]")
    LOGIN_INPUT = (By.XPATH, "//*[@id='username']/label/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='password']/label/input")
    ENTER_BUTTON = (By.XPATH, "/html/body/app-root/app-login/div[1]/div/div/button")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "/html/body/app-root/app-login/div[1]/div/div/a")

class EnterPageLocators():
    RECORD_PREVIEW = (By.XPATH, "//*[@id='rec323763270']")
    RECORD_ALARM = (By.ID, "rec459232823")
    # RECORD3 = (By.ID, "rec323763275")
    RECORD_FORGOT_PASSWORD = (By.ID, "rec323777085")
    RECORD_FORGOT_LOGIN = (By.ID, "rec323763281")
    RECORD_MEMO = (By.ID, "rec323790013")
    RECORD_TEAM = (By.ID, "rec341522139")
    RECORD_SCHEDULE = (By.ID, "rec323815254")
    RECORD_PROMO = (By.ID, "rec323805199")
    RECORD_NEED_HELP = (By.ID, "rec323824490")