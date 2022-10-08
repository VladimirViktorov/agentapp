from selenium.webdriver.common.by import By

class BasePageLocators():
    pass

class LoginPageLocators():
    CONTAINER_LOGINFORM = (By.XPATH, "/html/body/app-root/app-login/div[1]")
    CONTAINER_INFORMATION = (By.XPATH, "/html/body/app-root/app-login/div[2]")
    LOGIN_INPUT = (By.XPATH, "//*[@id='username']/label/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='password']/label/input")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//*[@id='password']/label/button")
    ENTER_BUTTON = (By.XPATH, "/html/body/app-root/app-login/div[1]/div/div/button")
    PASSWORD_RECOVERY_LINK = (By.XPATH, "/html/body/app-root/app-login/div[1]/div/div/a")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//*[@id='username']/ui-field-error")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//*[@id='password']/ui-field-error")

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

class PasswordRecoveryPageLocators():
    LOGIN_INPUT = (By.XPATH, "//*[@id='username']/label/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='password']/label/input")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//*[@id='password']/label/button")
    REPEAT_PASSWORD_INPUT = (By.XPATH, "//*[@id='repeatPassword']/label/input")
    SHOW_REPEAT_PASSWORD_BUTTON = (By.XPATH, "//*[@id='repeatPassword']/label/button")
    SEND_BUTTON = (By.XPATH, "/html/body/app-root/app-password-recovery/div/div/div/button")
    LOGIN_LINK = (By.XPATH, "/html/body/app-root/app-password-recovery/div/div/div/a")
    REPEAT_BUTTON = (By.XPATH, "/html/body/app-root/app-password-recovery/div/div/app-password-recovery-form/ui-form/div/a")
    VERIFICATION_CODE_INPUT = (By.XPATH, "//*[@id='token']/form/label/input")
    