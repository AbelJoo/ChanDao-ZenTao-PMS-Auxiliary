#! /usr/bin/python
# coding:utf-8
import os
import time
from bean import BugBean
import zen_tao_client


def scanner_config():
    """
    读取配置文件
    :return:
    """
    with open("config.inf", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("#"):
            lines.remove(line)
    kv_map = {}
    for line in lines:
        kv = line.strip().split(":", 1)
        kv_map[kv[0]] = kv[1]
    return kv_map

if __name__ == '__main__':
    kv_map = scanner_config()
    zen_tao_client.ACCOUNT = kv_map["account"]
    zen_tao_client.PASSWORD = kv_map["password"]
    print(kv_map)

    while True:
        bug_bean = zen_tao_client.get_my_bug()
        msg_title = None
        msg_content = None

        if len(bug_bean) != 0:
            msg_title = "当前共有" + str(len(bug_bean)) + "条bug"
            msg_content = "\t\n当前最新:\n\t\n"
            for bean in bug_bean:
                msg_content += bean.title + "\n\t\n"
                msg_content += "级别：" + bean.level + "\n"\
                               + "类型：" + bean.error_type + "\n"\
                               + "From:" + bean.author
        else:
            msg_title = "当前共有" + str(len(bug_bean)) + "条bug"
            msg_content = "无"

        if msg_title\
                and msg_content:
            os.system("notify-send -u critical "
                      + "\""
                      + msg_title
                      + "\""
                      + " "
                      + "\""
                      + msg_content
                      + "\"")
        time.sleep(13)