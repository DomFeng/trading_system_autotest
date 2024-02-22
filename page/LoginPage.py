#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/22 18:21
# @Author: fengjianguang

from base.LoginBase import LoginBase


class LoginPage(LoginBase):
    def login_input_value(self, driver, input_placeholder, value):
        """
        输入框输入值
        :param driver:
        :param input_placeholder:
        :param value:
        :return:
        """
        driver.find_element_by_xpath(self.login_input(input_placeholder)).send_keys(value)

    def login_button_click(self, driver, button_name):
        """
        点击按钮
        :param driver:
        :param button_name:
        :return:
        """
        driver.find_element_by_xpath(self.login_button(button_name)).click()
