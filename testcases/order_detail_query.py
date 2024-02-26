#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/23 18:44
# @Author: fengjianguang

from time import sleep
from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.OrderDetailPage import OrderDetailPage
# from . import __init__ as init


class TestOrderDetailQuery:
    def test_order_detail_query(self, driver):
        LeftMenuPage().level_two_menu_click(driver, "已卖出的宝贝")
        sleep(1)
        OrderDetailPage().order_detail_query(driver, "全部")
        sleep(1)
