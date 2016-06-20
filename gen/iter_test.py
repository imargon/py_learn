#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 运算符通常由左向右结合，即具有相同优先级的运算符按照从左向右的顺序计算。
# 从右向左运算：单目运算符，条件运算符，赋值运算符，其他的从左向右
# 例如，2 + 3 + 4被计算成(2 + 3) + 4。一些如赋值运算符那样的运算符是由右向左结合的，即a = b = c被处理为a = (b = c)。
from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'zhen'

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 # 初始化两个计数器a，b

    def __iter__(self):
        return self       #实例本身就是迭代对象，故返回自己

    def next(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 100000:   # 退出循环的条件
            raise StopIteration();
        return self.a        #返回a


for n in Fib():
    print n

# 迭代器是一个对象，而生成器是一个函数，迭代器和生成器是python中两个非常强大的特性，编写程序时你可以不使用生成器达到同样的效果，
# 但是生成器让你的程序更加pythonic。创建生成器非常简单，只要在函数中加入yield语句即可。
# 函数中每次使用yield产生一个值，函数就返回该值，然后停止执行，等待被激活，被激活后继续在原来的位置执行。下边的例子实现了同样的功能：

print  '***********************************';

def fib():
    a,b = 0,1
    while 1:
        a,b = b,a+b
        yield a
    for f in fib():
        if f< 10000:
            print f
        else:
            break

myDict = {'a':1,'b':2,'c':3,'d':4}
for eachKey in myDict:
    print eachKey,myDict[eachKey]
    del myDict[eachKey]

# 简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
def fab1(max):
    n,a,b = 0,0,1
    L=[]
    while n<max:
        L.append(b)
        a,b = b,a+b
        n = n + 1
    return L

def fab2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1

for m in fab2(10):
    print m

def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

def fab2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1














