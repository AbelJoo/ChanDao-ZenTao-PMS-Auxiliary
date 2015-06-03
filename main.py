#! /usr/bin/python
# coding:utf-8
import Tkinter
import pynotify
import zen_tao_client


if __name__ == '__main__':
    zen_tao_client.ACCOUNT = "zjj"
    zen_tao_client.PASSWORD = "123456"
    zen_tao_client.get_my_bug()
