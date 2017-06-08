#!/usr/bin/python
# coding=utf-8

from selenium import webdriver
import time
import os
import unittest
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

global driver

class TEST(unittest.TestCase):

    def setup(self):
        desired_caps = {}


        desired_caps['']='appium'
        desired_caps['platformName'] = 'Android'

        desired_caps['platformVersion'] = '5.0.2'

        desired_caps['deviceName'] = '520986ff'

        desired_caps['appPackage'] = 'com.aazen.companion'

        desired_caps['appActivity'] = 'com.aazen.companion.main.LauncherActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown(self):
        self.driver.quit()

    def login(self):

        self.driver.find_element_by_id('com.aazen.companion:id/user_login').click()
        self.driver.find_element_by_id('com.aazen.companion:id/user_mobile').send_keys('18362749811')
        self.driver.find_element_by_id('com.aazen.companion:id/user_password').send_keys('123456')
        self.driver.find_element_by_id('com.aazen.companion:id/user_login').click()  # 登录

        time.sleep(5)
        self.driver.find_element_by_id('com.aazen.companion:id/btn_disconnect').click()
        time.sleep(10)
        self.driver.find_element_by_id('com.aazen.companion:id/rl_title').click()  # 进入计步界面
        time.sleep(5)




if __name__ == '__main__':
    TEST()
