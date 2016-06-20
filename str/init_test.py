#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#  __init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性，
#  做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
#  __new__ 通常用于控制生成一个新实例的过程。它是类级别的方法。
#  __new__方法的调用是发生在__init__之前的
# 依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。


class Person(object):
    def __init__(self, name, age):
        print '__init called'
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        print '__new__ called.'
        return super(Person, cls).__new__(cls, name, age)

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name,self.age)


class PositiveInteger(int):
    def __new__(cls, *value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))
i = PositiveInteger(-3)
print i


if __name__ == "__main__":
    zhen = Person('zhen peng', 26)
    print zhen