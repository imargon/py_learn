# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
__author__ = 'zhen'
import os
import sys
import codecs
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

type = sys.getfilesystemencoding()
print type
print os.getcwd()

conf_file="kreminder.conf"
conf = ConfigParser.ConfigParser()
conf.readfp(codecs.open(conf_file, "r", "utf-8-sig"))


#secs = conf.sections()
secs = conf.get("REST_INTERVAL","message")
print secs
print 'sections:',secs.decode(type).encode('mbcs')




















def run():
    print "hello"
if __name__ == "__main__":
    run()    