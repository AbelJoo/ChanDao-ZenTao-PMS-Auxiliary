#! /usr/bin/python
# coding:utf-8

import urllib2
import cookielib
from bean import BugBean
from parser import BaseParser, MyBugParser

ACCOUNT = ""
PASSWORD = ""

HOST = ""
__site_login = "user-login.html"
__site_home_page = "my/"
__site_my_bug = "my-bug.html"

__cookie = None

__cookie = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(__cookie)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)


def login():
    """
    登录
    :return: 登陆成功返回True
    """
    body_text_0 = "account="
    body_text_1 = "&password="
    body_text_2 = "&keepLogin%5B%5D=on&referer=http%3A%2F%2" \
                  + "F117.78.6.79%3A8081%2Fzentaopms%2Fwww%2Fmy%2F"

    post_data = body_text_0 \
                + ACCOUNT \
                + body_text_1 \
                + PASSWORD \
                + body_text_2

    __cookie.clear()
    text = __request_html(HOST + __site_login, post_data)
    status = text.find("失败")

    if status == -1:
        print("登录成功")
        return True
    else:
        print("登录失败")
        return False


def __request_html(url, post_data=None):
    """
    成功返回html document，否则返回None
    :return: str
    """
    try:
        request = urllib2.Request(url, post_data)
        response = urllib2.urlopen(request, timeout=10)
        html_doc = str(response.read())
        # print(html_doc)
    finally:
        return html_doc


def __request_data(url, parser):
    """
    请求数据
    :param url:
    :param parser:
    :return:
    """
    html_doc = __request_html(url)
    parser.feed(html_doc)


def get_my_bug():
    parser = MyBugParser()
    __request_data(HOST + __site_my_bug, parser)
    return parser.bean_list