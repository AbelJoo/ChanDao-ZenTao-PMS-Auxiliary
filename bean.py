#! /usr/bin/python
# coding:utf-8


class DataBean(object):
    def __init__(self, uid=0):
        self.uid = uid


class BugBean(DataBean):
    def __init__(self, uid, level, error_type, title, author="未知", content=""):
        DataBean.__init__(self, uid)
        self.level = level
        self.error_type = error_type
        self.title = title
        self.author = author
        self.content = content