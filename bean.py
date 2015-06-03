#! /usr/bin/python
# coding:utf-8


class DataBean(object):
    pass


class BugBean(DataBean):
    def __init__(self, bug_id, level, error_type, title, author="未知", content=""):
        self.bug_id = bug_id
        self.level = level
        self.error_type = error_type
        self.title = title
        self.author = author
        self.content = content