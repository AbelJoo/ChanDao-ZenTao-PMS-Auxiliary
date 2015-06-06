#! /usr/bin/python
# coding:utf-8
import threading
import time
import sys
import cache
import tools
import zen_tao_client


def start_my_bug_loop_task():
    def task():
        while True:
            bug_beans = zen_tao_client.get_my_bug()

            # 过滤结果，并将最新数据放入缓存
            new_beans = cache.filter_new("bug", bug_beans)
            cache.add("bug", bug_beans)

            if len(new_beans) != 0:
                tools.print_log(__name__ + "." + sys._getframe().f_code.co_name,
                                "本次显示的bug:" + str(new_beans))

                for bean in new_beans:
                    msg_title = "当前有Bug指向您"
                    msg_content = bean.title + "\n\t\n"
                    msg_content += "级别：" + bean.level + "\n" \
                                   + "类型：" + bean.error_type + "\n" \
                                   + "From:" + bean.author
                    tools.show_notify(msg_title, msg_content)
            else:
                pass

            if len(new_beans) != 0:
                sleep_time = len(new_beans) * 13
            else:
                sleep_time = 1
            time.sleep(sleep_time)

    task = threading.Thread(target=task, name="start_my_bug_task_loop")
    task.start()
    return task