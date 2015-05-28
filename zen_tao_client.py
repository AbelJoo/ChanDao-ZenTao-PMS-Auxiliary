#! /usr/bin/python
# coding:utf-8

import urllib2
import cookielib
from parser import BaseParser, MyBugParser

ACCOUNT = ""
PASSWORD = ""

__site_host = "http://117.78.6.79:8081/zentaopms/www/"
__site_login = __site_host + "user-login.html"
__site_home_page = __site_host + "my/"
__site_my_bug = __site_host + "my-bug.html"

__cookie = None

__cookie = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(__cookie)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)


class DataBean(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content


def __login():
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
    request = urllib2.Request(__site_login, post_data)
    response = urllib2.urlopen(request)
    text = str(response.read())
    status = text.find("失败")

    if status == -1:
        print("登录成功")
        return True
    else:
        print("登录失败")
        return False


def __request_html(url):
    """
    成功返回html document，否则返回None
    :return: str
    """

    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_doc = str(response.read())
    # print(html_doc)
    return html_doc


def __request_data(url, parser):
    """
    请求数据
    :param url: url地址
    :param parser: 解释器，仅接收一个参数的函数
    :return: 解析成功返回DataBean，否则为None
    """



    ######################
    __login()
    html_doc = __request_html(url)
    # print(html_doc)

    parser = MyBugParser()
    parser.feed(html_doc)
    print("=================================")
    print(parser.tag_stack)

    ######################
    # beans = map(parser, html_doc)


    # beans = None
    #
    # if beans is None:
    #     __login()
    #     html_doc = __request_html(url)
    #     beans = map(parser, html_doc)
    #
    # return beans


def get_my_bug():
    __request_data(__site_my_bug, None)