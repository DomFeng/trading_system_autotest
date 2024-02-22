#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/8 0:48
# @Author: fengjianguang

import datetime
import os


def get_now_time():
    return datetime.datetime.now()


def get_project_path():
    """
    获取项目绝对路径
    :return:
    """
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    """
    为路径添加分隔符
    :param path: 路径
    :param add_sep_before: 是否在路径前添加分隔符
    :param add_sep_after: 是否在路径后添加分隔符
    :return:
    """

    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


if __name__ == "__main__":
    print(get_now_time())
    print(get_project_path())
    print(sep(["config", "environment.yaml"], add_sep_before=True))
