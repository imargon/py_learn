#-*- coding:utf-8 -*-
import os,sys,string
output = open('output.txt', 'w')
for root,dirs,files in os.walk('.'):
    for f  in files:
        print f
        output.write(f + '\n')
