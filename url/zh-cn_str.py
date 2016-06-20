#encoding:utf-8
s = '\u674e\u6587\u660a'
s
print s.decode("unicode-escape")
#另外一种方法在s前加u
s1 = u'\u674e\u6587\u660a'
print s1