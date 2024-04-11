#https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id= "Email"
    textbox_password_id= "Password"
    button_login_xpath= "//button[normalize-space()='Log in']"
    link_logout_linktext ="Logout"

    def __init__(self,driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

