from selenium.webdriver.common.by import By

from config.config import TestData
from pages.basepage import BasePage
from pages.homepage import HomePage


class LoginPage(BasePage):

    """By locators"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "loginBtn")
    SIGNUP = (By.LINK_TEXT, "Sign up")

    """Constructor of page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Get the page title"""
    def login_page_title(self, title):
        return self.get_title(title)

    """Check signup link is visible or not"""
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP)

    """Login to app"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN)
        return HomePage(self.driver)
