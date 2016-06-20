#encoding:utf-8
__author__ = 'zhen'

import os
path = "D:\py\str\sample.txt"

def make_text_file():
    a = open('test.txt',"w")
    a.write("This is how you create a new text file!")
    a.close()

def make_another_file():
    if os.path.isfile('test.txt'):
        print("You are trying to create a file that already exists!")
    else:
        f = open('test.txt',"w")
        f.write("This is how you create a new test file")

def add_some_text():
    a = open('test.txt',"a")
    a.write("Here is some additional text!")

def even_more_text():
    a = open("test.txt","a")
    a.write("""
    Here is more
    test"""
    )

def read_text():
    b = open('test.txt',"r")
    print b.read()
    b.close()

def print_line_lengths():
    c=open("test.txt","r")
    text = c.readlines()
    for line in text:
        print(len(line))
    c.close()

make_text_file()
make_another_file()
add_some_text()
even_more_text()
read_text()
print_line_lengths()