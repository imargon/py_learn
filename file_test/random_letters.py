#encoding :utf-8
__author__ = 'zhen'
import random,string

def GenPassword(length):
    chars=string.ascii_letters+string.digits
    print random.choice(chars)
    print ([random.choice(chars) for i in range(length)])
    print ''.join([random.choice(chars) for i in range(length)])

GenPassword(12)

# if __name__ == "__main__":
#     for i in range(10):
#         print  GenPassword(10)

str = "+"
seq= ("a","b","c")
print str.join(seq)