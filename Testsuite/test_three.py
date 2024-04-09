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
@pytest.mark.demo
def test_three_01():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()
def test_facebook():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"
    driver.quit()
def test_python1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.python.org/")
    assert driver.title == "Welcome to Python.org"
    driver.quit()

