#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/23 18:41
# @Author: fengjianguang

from base.OrderDetailBase import OrderDetailBase


class OrderDetailPage(OrderDetailBase):
    def order_detail_query(self, driver, status):
        """
        订单详情查询
        :param driver:
        :param status:
        :return:
        """
        driver.find_element_by_xpath(self.order_status(status)).click()
