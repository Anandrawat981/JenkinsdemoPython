#https://petdiseasealerts.org/forecast-map#/
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class MapLoginPage:
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    def __init__(self,driver):
        self.driver = driver

    def setmapElements(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://petdiseasealerts.org/forecast-map#/")
        self.frame1 = self.driver.find_element(By.XPATH,"//iframe[starts-with(@id,'map-instance')]")
        self.driver.switch_to.frame(self.frame1)
        mapelements = self.driver.find_elements(By.XPATH,"//*[@id='regions']")
        f = open("maptest.txt", "a+")
        for mapele in mapelements:
            print(mapele.text)

            f.write(mapele.text+'\n')
        f.close()



