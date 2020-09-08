# encoding:utf-8

from selenium.webdriver.common.by import By
from .basePage import Page
from time import sleep

class login(Page):

    url = '/#/login'
    login_username_loc = (By.XPATH,"//div[@id='main']/div/div/form/div/div/div/input")
    login_passwrd_loc = (By.XPATH, "//input[@type='password']")
    login_button_loc = (By.XPATH, "//button[@type='button']")

    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_passwrd_loc).clear()
        self.find_element(*self.login_passwrd_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def get_loginpage_handle(self):
        self.open()
        loginpage_handle = self.driver.current_window_handle
        return loginpage_handle

    def user_login(self, username='', password=''):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)


    def user_login_sucess(self):
        return self.driver.title

    
