#! /usr/bin/python
# coding:utf-8

from sgmllib import SGMLParser


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

    def handle_data(self, text):
        # id
        if cmp(tuple(self.tag_stack), MyBugParser.__id_stack__) == 0 \
                and self.is_now_has_tag_key(MyBugParser.__id_tag_key_set__):
            print("issues id: " + text)