import pytest
from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver= ch_driver
    yield
    ch_driver.close()

@pytest.fixture(scope='class')
def init_firefox_driver(request):
    ff_driver= webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver=ff_driver
    yield
    ff_driver.close()
@pytest.mark.usefixtures('init_chrome_driver')
class Base_chrome_Test:
    pass

class Test_Google_chrome(Base_chrome_Test):
    def test_google_chrome_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"

@pytest.mark.usefixtures('init_firefox_driver')
class Base_firefox_Test:
    pass

class Test_Google_firefox(Base_firefox_Test):
    def test_google_firefox_title(self):
        self.driver.get("https://www.youtube.com/")
        assert self.driver.title == "YouTube"