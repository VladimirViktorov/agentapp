from selenium.webdriver.common.by import By

class BasePageLocators():
    pass

class LoginPageLocators():
    CONTAINER_LOGINFORM = (By.XPATH, "/html/body/app-root/app-login/div[1]")
    CONTAINER_INFORMATION = (By.XPATH, "/html/body/app-root/app-login/div[2]")