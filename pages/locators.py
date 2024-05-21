from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators():
    LOGIN_BUTTON = (By.XPATH, "//button[@name='login_submit']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    LOGIN_URL = (By.XPATH, "//a[@id='login_link']")
