#!/usr/bin/python
# coding=utf-8

from selenium import webdriver

import time
import os
import unittest

from lib2to3.tests.support import driver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))




class  TEST(unittest.TestCase):

    def setup(self):
        desired_caps = {}

        desired_caps['automationName'] = 'Appium'

        desired_caps['platformName'] = 'Android'

        desired_caps['platformVersion'] = '5.0.2'

        desired_caps['deviceName'] = '520986ff'

        desired_caps['appPackage'] = 'com.aazen.companion'

        desired_caps['appActivity'] = 'com.aazen.companion.main.LauncherActivity'

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver.find_element_by_id('com.aazen.companion:id/user_login').click()
        driver.find_element_by_id('com.aazen.companion:id/user_mobile').send_keys('18362749811')
        driver.find_element_by_id('com.aazen.companion:id/user_password').send_keys('123456')
        driver.find_element_by_id('com.aazen.companion:id/user_login').click()  # 登录

        time.sleep(5)
        driver.find_element_by_id('com.aazen.companion:id/btn_disconnect').click()
        time.sleep(10)
        driver.find_element_by_id('com.aazen.companion:id/rl_title').click()  # 进入计步界面
        time.sleep(5)

        def getSize():
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            return (x, y)

        def swipeDown(t):
            l = getSize()
            x1 = int(l[0] * 0.5)
            y1 = int(l[1] * 0.25)
            y2 = int(l[1] * 0.75)
            driver.swipe(x1, y1, x1, y2, t)

        swipeDown(1000)

        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
