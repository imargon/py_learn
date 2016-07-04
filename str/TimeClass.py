#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time1(self):
        print ('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def print_time2(time):
        print ('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 32


def run():
    print "hello"


if __name__ == "__main__":
    run()
    print_time2(start)