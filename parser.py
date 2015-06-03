#! /usr/bin/python
# coding:utf-8

from sgmllib import SGMLParser
from bean import DataBean, BugBean


class BaseParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.tag_stack = []
        self.now_tag_attrs = []

    def finish_starttag(self, tag, attrs):
        SGMLParser.finish_starttag(self, tag, attrs)
        self.now_tag_attrs = {} if attrs is None else attrs
        self.tag_stack.append(tag)
        # print("start_tag: " + str(self.tag_stack))
        # print("start_attrs: " + str(attrs))

    def finish_endtag(self, tag):
        SGMLParser.finish_endtag(self, tag)
        self.now_tag_attrs = {}
        # 一直pop，直到踢出与当前endtag匹配的为止。
        # 这种现象是由于出现<meta/>这种只有starttag的标签导致的
        while True:
            if cmp(tag, self.tag_stack[-1]) == 0:
                self.tag_stack.pop()
                break
            else:
                self.tag_stack.pop()
        # print("  end_tag: " + str(self.tag_stack))

    def is_now_has_tag_key(self, key_set):
        if not self.now_tag_attrs \
                and not key_set:
            return True
        elif not self.now_tag_attrs \
                or not key_set:
            return False

        for key in key_set:
            kv_index = 0
            for kv in self.now_tag_attrs:
                kv_index += 1
                if cmp(key, kv[0]) == 0:
                    break
                if len(self.now_tag_attrs) == kv_index:
                    return False
        return True

    def get_data(self):
        pass


class MyBugParser(BaseParser):
    __id_stack__ = ("html", "body", "div", "div", "form", "table", "tbody", "tr", "td", "input", "a")
    __id_tag_key_set__ = ("href", "target")
    __level_stack__ = ("html", "body", "div", "div", "form", "table", "tbody", "tr", "td", "span")
    __level_tag_key_set__ = ("class",)
    __title_stack__ = ("html", "body", "div", "div", "form", "table", "tbody", "tr", "td", "a")
    __title_tag_key_set__ = ("href",)
    # 直接被<td>标签包裹的元素
    __td_stack__ = ("html", "body", "div", "div", "form", "table", "tbody", "tr", "td")
    __td_tag_key_set__ = ()

    def __init__(self):
        BaseParser.__init__(self)
        self.content_set = []
        self.bean_list = []

    def handle_data(self, text):
        # id
        if cmp(tuple(self.tag_stack), MyBugParser.__id_stack__) == 0 \
                and self.is_now_has_tag_key(MyBugParser.__id_tag_key_set__):
            self.add_to_content_set(text)
            print("bug id: " + text)
        # level
        if cmp(tuple(self.tag_stack), MyBugParser.__level_stack__) == 0 \
                and self.is_now_has_tag_key(MyBugParser.__level_tag_key_set__):
            self.add_to_content_set(text)
            print("bug level: " + text)
        # title
        if cmp(tuple(self.tag_stack), MyBugParser.__title_stack__) == 0 \
                and self.is_now_has_tag_key(MyBugParser.__title_tag_key_set__):
            self.add_to_content_set(text)
            print("bug title: " + text)
        # td
        if cmp(tuple(self.tag_stack), MyBugParser.__td_stack__) == 0 \
                and self.is_now_has_tag_key(MyBugParser.__td_tag_key_set__) \
                and str(text).strip() != "":
            self.add_to_content_set(text)
            print("bug <td> tag: " + text)

    def add_to_content_set(self, value):
        self.content_set.append(value)
        if len(self.content_set) == 6:
            bean = BugBean(self.content_set[0],
                           self.content_set[1],
                           self.content_set[2],
                           self.content_set[3],
                           self.content_set[4])
            self.bean_list.append(bean)
            self.content_set = []