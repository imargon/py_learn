#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'

print np.__version__
z = np.zeros((3,5))
print z
z[1,2] = 1
print z
z1= np.arange(1,101)
print z1






def run():
    print "hello"


if __name__ == "__main__":
    run()    