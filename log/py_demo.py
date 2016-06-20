#encoding:gbk
import platform
import sys

print platform.python_version()
print sys.version
print sys.version_info



for letter in 'Python':
    if letter == 'h':
        continue
    print u'当前字母：',letter
    
    
var = 10
while var>0:
    var = var- 1
    if var ==5:
        continue
    print u'当前：',var
print "Good bye" 

