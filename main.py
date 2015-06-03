#! /usr/bin/python
# coding:utf-8
import os
import time
from bean import BugBean
import zen_tao_client


if __name__ == '__main__':
    zen_tao_client.ACCOUNT = "zjj"
    zen_tao_client.PASSWORD = "123456"

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