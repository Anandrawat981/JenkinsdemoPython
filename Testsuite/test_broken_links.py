import pytest
import requests
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestBase:
    pass

class Test_Brokenlinks(TestBase):
    @pytest.mark.smoke
    def test_brokenlinks_flipkart(self):
        global res
        f=open("brokenlink.txt","a+")
        self.driver.get("http://www.deadlinkcity.com/")
        allLinks=self.driver.find_elements(By.TAG_NAME,"a")
        print(len(allLinks),"is length of link.")
        count=0
        for link in allLinks:
            url = link.get_attribute("href")
            try:
                res = requests.head(url)
            except:
                None
            if res.status_code >= 400:
                print("Is broken link")
                f.write(url+'\n')
                count+=1
            else:
                f1=open("NotbrokenLinks.txt","a+")
                f1.write(url+'\n')
                print("not broken link")
        print(count,"Total no of broken links")
        print(len(allLinks)-count,"Total no of unbroken links")

