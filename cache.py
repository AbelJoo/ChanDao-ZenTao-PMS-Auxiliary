#! /usr/bin/python
# coding:utf-8


__val_dict = {}


def filter_new(key, bean_list):
    old_bean_id = [old_bean.uid for old_bean in __val_dict.get(key, {})]
    return [bean.uid for bean in bean_list if bean.uid not in old_bean_id]


def add(key, bean_list):
    __val_dict[key] = bean_list