#encoding:utf-8
from __future__ import unicode_literals

import os,sys,stat,time,locale
import string,StringIO
import shutil
#shutil.copytree（ResDir,DesDir）#拷贝
#shutil.rmtree(Dir)#删除

# 如果文件夹为空则删除，否则将文件夹下的所有文件移动到一个新文件夹
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
path="E:/newfile/"
os.chdir(path)

def p(f):
    print '%s.%s(): %s' %(f.__module__,f.__name__,f())
    p(sys.getdefaultencoding())  # 返回当前系统所使用的默认字符编码
    p(sys.getfilesystemencoding())  # 返回用于转换Unicode文件名至系统文件名所使用的编码
    p(locale.getdefaultlocale())  # 获取默认的区域设置并返回元祖(语言, 编码)
    p(locale.getpreferredencoding) # 返回用户设定的文本数据编码
    print r" '\xba\xba'.decode('mbcs'):",repr('\xba\xba'.decode('mbcs'))


def file_os(path):
    filepath = os.getcwd()
#    new_path = os.mkdir(path+"myfile2")
    for filename in os.listdir(path):
        fpath = os.path.join(filepath,filename)   # 拼接文件路径和路径下面的文件名
        ifdir = os.path.isdir(fpath)              # 是否是文件夹

        #fpath = unicode(os.path.join(filepath,filename).replace('\\','/'),'utf-8')   # 拼接文件路径和路径下面的文件名
        #ifdir = unicode(os.path.isdir(fpath),'utf-8')  # 是否是文件夹
        #print fpath
        if ifdir:
            temppath2 = os.listdir(fpath)  #如果是文件夹，获取下面的文件
            for temppath3 in temppath2:
                fpath2 = os.path.join(fpath,temppath3)  #文件夹中的绝对路径
                temp3  = os.path.splitext(temppath3)  #分割文件名与文件后缀
                print str(temp3)
                #new_path.close()
                #if temp3[1] == '.wmv': #temp3[0]是文件名，temp3[1]是文件名后缀，文件是MP4 格式的
                #shutil.move(fpath2,filepath)
        else:
            os.rmdir(fpath) #rmdir()函数来删除空目录，如果删除的目录中存在子文件夹或者文件则会抛出异常

for root,dirs,files in os.walk(path):
    for name in dirs:
        if dirs != [] and files !=[]:
            print str(dirs)
        else:
            os.rmdir(os.path.join(root, name))

file_os(path)

print('**************')



