#! /usr/bin/python
# coding:utf-8


class DataBean(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content