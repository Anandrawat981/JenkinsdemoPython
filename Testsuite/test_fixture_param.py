import pytest
from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#This code will be run both in chrome and firefox parallel
@pytest.fixture(params=["chrome","firefox"],scope='class')
def init_driver(request):
    global web_driver
    if request.param=="chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param =="firefox":
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("setup")
class BaseTest:
    pass


class Test_Google(BaseTest):
    @pytest.mark.skip
    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"


