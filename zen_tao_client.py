#! /usr/bin/python
# coding:utf-8

import urllib2
import cookielib

_host = "http://117.78.6.79:8081/zentaopms/www/"
_login = _host + "user-login.html"
_home_page = _host + "my/"
_my_bug = _host + "my-bug.html"

_cookie = None

_cookie = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(_cookie)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)


class Login(object):
    def __init__(self, account, password):
        self.account = account
        self.password = password

    def login(self):
        """
        登录
        :return: 登陆成功返回True
        """
        body_text_0 = "account="
        body_text_1 = "&password="
        body_text_2 = "&keepLogin%5B%5D=on&referer=http%3A%2F%2" \
                      + "F117.78.6.79%3A8081%2Fzentaopms%2Fwww%2Fmy%2F"

        post_data = body_text_0 \
                    + self.account \
                    + body_text_1 \
                    + self.password \
                    + body_text_2

        _cookie.clear()
        request = urllib2.Request(_login, post_data)
        response = urllib2.urlopen(request)
        text = str(response.read())
        status = text.find("失败")

        if status == -1:
            print("登录成功")
            return True
        else:
            print("登录失败")
            return False


class DataBean(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content


class Operation(object):
    def __init__(self, login):
        self.login = login
        self.url = None

    def get_data(self):
        """
        成功返回数据，否则返回None
        :return: list
        """

        html_doc = self.request_html()
        if html_doc is None:
            self.login.login()
            html_doc = self.request_html()
        beans = self.parser_html(html_doc)
        return beans

    def request_html(self):
        """
        成功返回html document，否则返回None
        :return: str
        """

        request = urllib2.Request(self.url)
        response = urllib2.urlopen(request)
        html_doc = str(response.read())
        print(html_doc)
        return html_doc

    def parser_html(html_doc):
        """
        解析html document
        :rtype : list
        """
        pass


class HomePage(Operation):
    def __init__(self, login, url=_home_page):
        Operation.__init__(self, login)
        self.url = url


class MyBug(Operation):
    def __init__(self, login, url=_my_bug):
        Operation.__init__(self, login)
        self.url = url

        def parser_html(html_doc):
            pass