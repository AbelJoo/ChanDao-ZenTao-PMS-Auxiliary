#! /usr/bin/python
# coding:utf-8
import threading
import time
import sys
import signal
from bean import BugBean
import cache
import loop_task
import tools
import zen_tao_client


VERSION = "1.0 Beta"


def exit_handler(signum, frame):
    tools.print_log(__name__ + "." + sys._getframe().f_code.co_name,
                    "exit sign"
                    + "\nsignum=" + str(signum)
                    + "\nframe=" + str(frame))
    loop_task.RUN = False


def execute():
    """
    # 从这里开始执行程序
    :return:
    """

    ###########################################################
    # 第零步：捕获终止信号量ready
    ###########################################################
    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)

    ###########################################################
    # 第一步：读取配置文件并配置
    ###########################################################
    kv = tools.scanner_config()
    zen_tao_client.ACCOUNT = kv["account"]
    zen_tao_client.PASSWORD = kv["password"]
    zen_tao_client.HOST = kv["host"]

    ###########################################################
    # 第二步：进行登录
    ###########################################################
    is_login_success = zen_tao_client.login()
    if is_login_success:
        msg_title = "登录成功"
        msg_content = kv["account"] + " 已登录"
        msg_content += "\n\t\n当前版本：" + VERSION
    else:
        msg_title = "登录失败"
        msg_content = "请检查:\n" \
                      + "-您的用户名或密码是否正确\n" \
                      + "-您的host地址是否正确填写\n" \
                      + "-网络连接是否正常\n" \
                      + "\t\n当前版本：" + VERSION
    tools.show_notify(msg_title, msg_content)

    if not is_login_success:
        return

    ###########################################################
    # 第三步：开始任务
    ###########################################################
    threads = []

    task = loop_task.get_my_bug_loop_task()
    task.setDaemon(True)
    threads.append(task)

    for t in threads:
        t.start()

    ###########################################################
    # 第四步：进程终止流程
    ###########################################################
    while True:
        alive = False
        for t in threads:
            alive = alive or t.isAlive()
        if not alive:
            break
        else:
            time.sleep(1)

    tools.show_notify("ZenTao-PMS-Auxiliary 已终止运行",
                      "脚本已终止")


if __name__ == '__main__':
    execute()