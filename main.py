#! /usr/bin/python
# coding:utf-8
import threading
import time
import tools
import zen_tao_client


VERSION = "0.1 Beta"


def run():
    """
    # 从这里开始执行程序
    :return:
    """
    ########################################
    # 第一步：读取配置文件并配置
    ########################################
    kv = tools.scanner_config()
    zen_tao_client.ACCOUNT = kv["account"]
    zen_tao_client.PASSWORD = kv["password"]
    zen_tao_client.HOST = kv["host"]

    ########################################
    # 第二步：进行登录
    ########################################
    is_login_success = zen_tao_client.login()
    if is_login_success:
        msg_title = "登录成功"
        msg_content = "当前版本：" + VERSION
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

    ########################################
    # 第三步：开始任务
    ########################################
    start_my_bug_task_loop()


def start_my_bug_task_loop():
    def task():
        while True:
            time.sleep(45)
            bug_bean = zen_tao_client.get_my_bug()

            if len(bug_bean) != 0:
                msg_title = "当前共有" + str(len(bug_bean)) + "条bug"
                msg_content = "\t\n当前最新:\n\t\n"
                for bean in bug_bean:
                    msg_content += bean.title + "\n\t\n"
                    msg_content += "级别：" + bean.level + "\n" \
                                   + "类型：" + bean.error_type + "\n" \
                                   + "From:" + bean.author
            else:
                msg_title = "当前共有" + str(len(bug_bean)) + "条bug"
                msg_content = "无"

            if msg_title and msg_content:
                tools.show_notify(msg_title, msg_content)

    task = threading.Thread(target=task, name="start_my_bug_task_loop")
    task.start()
    return task


if __name__ == '__main__':
    run()