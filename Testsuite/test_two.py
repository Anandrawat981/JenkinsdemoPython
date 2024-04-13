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
def test_two_02():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])
    driver.get("https://www.flipkart.com/")
    # next_button = driver.find_element(By.XPATH,"//*[@id='__next']/div/section/div/div/div[6]/div/div/div/div/div/div/div/div[2]/div[2]")
    # while(next_button==True):
    driver.implicitly_wait(10)
    elementone = driver.find_element(By.XPATH,"//*[text()='Grocery']").text
    print(elementone)

    # next_button.click()
@pytest.mark.demo
def test_two_03():
    str1='Pytest test'
    print(str1[::-1])

@pytest.mark.demo
def test_two_04():
    lst=['anand','rawat']
    print(lst[::-2])
