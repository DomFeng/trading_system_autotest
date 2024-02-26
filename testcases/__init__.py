#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/2 16:52
# @Author: fengjianguang

from config.driver_config import DriverConfig
from testcases.test_login import TestLogin
from testcases.order_detail_query import TestOrderDetailQuery

if __name__ == '__main__':
    driver = DriverConfig.driver_config()
    TestLogin().test_login(driver)
    TestOrderDetailQuery().test_order_detail_query(driver)
    driver.quit()
