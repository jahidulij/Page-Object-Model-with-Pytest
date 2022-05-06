import pytest
from selenium import webdriver

from config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTEABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTEABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(5)
    yield
    web_driver.close()
