#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/2/6 19:00
# @Author: fengjianguang
import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            print(self.env)

    def get_username_password(self):
        return self.env["username"], self.env["password"]

    def get_db(self):
        return self.env["mysql"]

    def get_url(self):
        return self.env["url"]


if __name__ == "__main__":
    print(GetConf().get_username_password())
    print(GetConf().get_db())
    print(GetConf().get_url())
