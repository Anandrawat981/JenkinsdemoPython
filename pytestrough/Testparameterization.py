import pytest
from selenium.webdriver.common.by import By


'''@pytest.mark.parametrize("num,result",[(1,11),(2,22),(3,33),(4,44)])
def test_parameter_calculation(num,result):
    assert 11*num == result '''

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TesthubsportTest(BaseTest):
    @pytest.mark.parametrize(
        "username,password",
        [
            ("admin123@gmail.com","admin123"),
            ("anand123@gmail.com","anand123"),
        ]


    )
    def test_login1(self,username,password):
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.XPATH,"//*[@id='username']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        #self.driver.find_element(By.XPATH, "//*[@id='username']").clear()
        #self.driver.find_element(By.XPATH, "//*[@id='password']").clear()

