#! /usr/bin/python
# coding:utf-8
from zen_tao_client import Login, Operation, HomePage, MyBug

if __name__ == '__main__':

    login = Login("zjj", "123456")
    login.login()

    home = HomePage(login)
    home.get_data()

    my_bug = MyBug(login)
    home.get_data()