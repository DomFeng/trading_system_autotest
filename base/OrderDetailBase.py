#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/23 18:30
# @Author: fengjianguang

class OrderDetailBase:
    def order_status(self, status):
        """
        订单状态
        :param status:
        :return:
        """
        return "//div[@role='tablist']/div[text()='" + status + "']"
