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
def setup_module(module):
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")

def teardown_module(module):
    driver.quit()
@pytest.mark.skip
def test_google_title():
    assert driver.title =="Google"

