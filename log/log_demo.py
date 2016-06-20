#coding:utf-8


import sys,logging,datetime,time
logging.basicConfig(level=logging.INFO,
                    format='levelname:%(levelname)s filename: %(filename)s '
                           'outputNumber:[%(lineno)d] thread: %(threadName)s output msg: %(message)s'
                           '-%(asctime)s',datefmt='[%d%b%Y %H:%M:%S]',
                    filename='d:/py/log/loggmsg.log')
logging.info('Hi,Leon')

def test():
    now_time = time.time()
    a = 10
    a += 2
    b = 'test string'
    print a,now_time

if __name__ == '__main__':
    test()

