# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import codecs
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'

conf_file="kreminder.conf"
config = ConfigParser.ConfigParser()
config.readfp(codecs.open(conf_file, "r", "utf-8-sig"))
#interval = config.get("REST_INTERVAL","message")
todo_list = config.get("TODO_LIST","hi")
#print interval
print todo_list
