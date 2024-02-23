#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/23 16:35
# @Author: fengjianguang

class HomeBase:
    def wallet_swtich(self):
        """
        首页的钱包开关
        :return:
        """
        return "//span[contains(@class,'el-switch__core')]"

    def logo(self):
        """
        首页左上角的logo
        :return:
        """
        return "//div[contains(text(),'校园二手交易')]"

    def welcome(self):
        """
        首页欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"