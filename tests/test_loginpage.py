import pytest

from config.config import TestData
from pages.loginpage import LoginPage
from tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)