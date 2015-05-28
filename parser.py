#! /usr/bin/python
# coding:utf-8

from sgmllib import SGMLParser


class BaseParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.tag_stack = []

    def finish_starttag(self, tag, attrs):
        SGMLParser.finish_starttag(self, tag, attrs)
        self.tag_stack.append(tag)
        print("start_tag: " + str(self.tag_stack))

    def finish_endtag(self, tag):
        SGMLParser.finish_endtag(self, tag)
        # 一直pop，直到踢出与当前endtag匹配的为止。
        # 这种现象是由于出现<meta/>这种只有starttag的标签导致的
        while True:
            if cmp(tag, self.tag_stack[-1]) == 0:
                self.tag_stack.pop()
                break
            else:
                self.tag_stack.pop()
        print("  end_tag: " + str(self.tag_stack))

    def handle_data(self, text):
        pass


class MyBugParser(BaseParser):
    pass