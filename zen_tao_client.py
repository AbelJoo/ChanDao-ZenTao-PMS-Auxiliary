#! /usr/bin/python
# coding:utf-8

import urllib2
import cookielib
import sys
from bean import BugBean
import cache
from parser import BaseParser, MyBugParser
import tools


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
    is_success = text.find("失败") == -1 and not cmp(text, "") == 0

    if is_success:
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
    html_doc = ""
    try:
        request = urllib2.Request(url, post_data)
        response = urllib2.urlopen(request, timeout=10)
        html_doc = str(response.read())
    except Exception as e:
        tools.print_log(__name__ + "." + sys._getframe().f_code.co_name,
                        "something error at:" + "\n"
                        + url
                        + "\nexception message:"
                        + str(e.message))
    finally:
        return html_doc


def __request_data(url, parser):
    """

    :param url:
    :param parser:
    :return: bean list
    """
    html_doc = __request_html(url)
    parser.feed(html_doc)
    tools.print_log(__name__ + "." + sys._getframe().f_code.co_name,
                    url + "\n" + str(parser.bean_list))
    return parser.bean_list


def get_my_bug():
    parser = MyBugParser()
    bean_list = __request_data(HOST + __site_my_bug, parser)
    return bean_list