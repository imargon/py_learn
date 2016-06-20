#coding:utf-8
from __future__ import unicode_literals

import os,sys,stat,time,locale
import chardet
import string,StringIO
import shutil
#shutil.copytree（ResDir,DesDir）#拷贝
#shutil.rmtree(Dir)#删除

# 如果文件夹为空则删除，否则将文件夹下的所有文件移动到一个新文件夹
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('UTF-8')
path="E:/newfile/"
os.chdir(path)

for root,dirs,files in os.walk(path):
    for name in dirs:
        if dirs != [] and files !=[]:
            print unicode(dirs,'utf-8').encode('gbk')
            print chardet.detect(dirs)
        else:
            os.rmdir(os.path.join(root, name))
        #os.system('rd /S /Q %s'%root)

unicode(os.path.join(os.path.dirname(__file__),'CtManage','templates').replace('\\','/'),"gb2312"),

unicode(os.path.join(os.path.dirname(__file__),'CtManage','templates').replace('\\','/'),"utf8"),

os.path.join(os.path.dirname(__file__),'CtManage','templates').replace('\\','/').encode("utf8")