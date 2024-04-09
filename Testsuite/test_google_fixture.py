import pytest
from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import requests as requests

#driver = None
#driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager.install()))
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------setup-------")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")
    yield
    print("--------teardown-------")
    driver.quit()

def test_google_title(init_driver):
    assert driver.title =="Google"
    print("Test case Passed")
@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url =="Google"
    print("Test case Failed")
