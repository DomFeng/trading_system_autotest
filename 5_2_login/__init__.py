#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/1 12:43
# @Author: fengjianguang

from config.driver_config import DriverConfig
from time import sleep
driver = DriverConfig().driver_config()
driver.get("http://www.tcpjwtester.top")

driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("1234abcd!")
sleep(1)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(2)
driver.quit()
