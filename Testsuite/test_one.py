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
def test_one_01():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])
    driver.get("https://www.noon.com/uae-en/")
    # next_button = driver.find_element(By.XPATH,"//*[@id='__next']/div/section/div/div/div[6]/div/div/div/div/div/div/div/div[2]/div[2]")
    # while(next_button==True):
    allelements = driver.find_elements(By.XPATH,
                                       "//*[@id='__next']/div/section/div/div/div[6]/div/div/div/div/div/div/div/div[2]/div[1]/div")
    print(len(allelements))
    
    # next_button.click()



