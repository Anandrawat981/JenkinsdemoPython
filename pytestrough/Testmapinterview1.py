#https://petdiseasealerts.org/forecast-map#/
from time import sleep

from selenium import webdriver
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



def test_setmapElements():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    driver.get("https://petdiseasealerts.org/forecast-map#/")
    driver.maximize_window()
    frame1 = driver.find_element(By.XPATH, "//iframe[starts-with(@id,'map-instance')]")
    driver.switch_to.frame(frame1)
    mapelements = driver.find_elements(By.XPATH, "//*[@id='regions']//*[@class='region']")
    print(len(mapelements))
    act = ActionChains(driver)

    f = open("maptest.txt", "a+")
    for mapele in mapelements:
        countryname=mapele.get_attribute("id")
        print(countryname)
        f.writelines(countryname+'\n')
        if countryname == 'florida':
            mapcountry=driver.find_element(By.XPATH,"//*[@class='rpath']//*[@name='Florida']")
            driver.execute_script("arguments[0].scrollIntoView();", mapcountry)
            driver.execute_script("return window.pageYoffset;")
            sleep(5)
            #mapcountry.click()
            #act.move_to_element(mapcountry).click().perform()
            act.double_click(mapcountry).perform()
            sleep(5)
    f.close()

