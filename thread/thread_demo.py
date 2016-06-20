#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
#from __future__ import unicode_literals
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'

def run():
    print "hello"

def get_thread_name():
    t = threading.current_thread()
    return t.name

# define a function for the thread
def print_time(delay):
    thread_name = get_thread_name()
    count = 0
    while count < 8:
        time.sleep(delay)
        count +=1
        print("%s :%s" %(thread_name,time.ctime(time.time())))

# create two threads as follows
t1 = threading.Thread(target=print_time,args=(1,))
t2 = threading.Thread(target=print_time,args=(2,))

t1.start()
t2.start()
t1.join()
t2.join()

if __name__ == "__main__":
    run()    