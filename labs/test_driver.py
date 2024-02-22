#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/22 17:39
# @Author: fengjianguang

from time import sleep
from config.driver_config import DriverConfig


driver = DriverConfig().driver_config()
driver.get("http://192.168.0.110")
sleep(4)
driver.quit()