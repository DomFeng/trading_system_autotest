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

    def show_date(self):
        """
        首页显示日期
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        """
        首页用户头像大图
        :return:
        """
        return "//span[contains(text(),'欢迎您')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar_2(self):
        """
        首页用户头像大图2
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"
