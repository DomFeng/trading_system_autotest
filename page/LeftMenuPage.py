#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/23 18:33
# @Author: fengjianguang

from base.LeftMenuBase import LeftMenuBase


class LeftMenuPage(LeftMenuBase):
    def level_one_menu_click(self, driver, menu):
        """
        点击一级菜单
        :param driver:
        :param menu:
        :return:
        """
        driver.find_element_by_xpath(self.level_one_menu(menu)).click()

    def level_two_menu_click(self, driver, menu):
        """
        点击二级菜单
        :param driver:
        :param menu:
        :return:
        """
        driver.find_element_by_xpath(self.level_two_menu(menu)).click()