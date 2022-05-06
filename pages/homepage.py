from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class HomePage(BasePage):

    HEADER = (By.CSS_SELECTOR, "h1.private-header__heading private-header__heading--solo")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "account-name ")
    SETTING_ICON = (By.XPATH, "//a[@id='navSetting']//*[@id='Layer_1']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_exist(self):
        return self.is_visible(self.SETTING_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

