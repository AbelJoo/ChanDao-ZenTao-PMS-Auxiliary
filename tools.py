#! /usr/bin/python
# coding:utf-8
import os
import time


def scanner_config():
    """
    读取配置文件
    :return: dict
    """
    with open("config.inf", "r") as f:
        lines = f.readlines()
    line_index = 0
    while line_index < len(lines):
        if lines[line_index].startswith("#"):
            lines.remove(lines[line_index])
            line_index -= 1
        line_index += 1
    kv_dict = {}
    for line in lines:
        kv = line.strip().split(":", 1)
        kv_dict[kv[0]] = kv[1]
    return kv_dict


def show_notify(title, content=""):
    msg = "notify-send -u critical " \
        + "\"" \
        + title \
        + "\"" \
        + " " \
        + "\"" \
        + "\t\n" \
        + content \
        + "\""
    os.system(msg)


def print_log(title, content):
    print ("============================================================")
    print (time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())) + str(title))
    print (content)
    print ("============================================================")