import pytest
from selenium.webdriver.common.by import By

from Pageobjects.ForecastMapPage import MapLoginPage
@pytest.mark.usefixtures("setup")
class BaseTest:
    pass

class Test_case_01_interview(BaseTest):

    def test_interview_prep(self):

        self.mp=MapLoginPage(self.driver)
        self.mp.setmapElements()
        '''self.driver.implicitly_wait(20)
        self.driver.get("https://petdiseasealerts.org/forecast-map#/")
        self.frame1 = self.driver.find_element(By.XPATH, "//iframe[starts-with(@id,'map-instance')]")
        self.driver.switch_to.frame(self.frame1)
        mapelements = self.driver.find_elements(By.XPATH, "//*[@id='regions']")

        for mapele in mapelements:
            print(mapele.text)'''

        print("Test case maping")





