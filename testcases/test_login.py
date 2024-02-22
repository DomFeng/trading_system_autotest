#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/22 18:29
# @Author: fengjianguang

from time import sleep
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig.driver_config()
        driver.get("http://192.168.0.110")
        sleep(3)
        LoginPage().login_input_value(driver, "用户名", "william")
        sleep(1)
        LoginPage().login_input_value(driver, "密码", "1234abcd!")
        sleep(1)
        LoginPage().login_button_click(driver, "登录")
        sleep(3)
        driver.quit()
