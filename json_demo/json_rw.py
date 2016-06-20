#!/usr/bin/env python
# -*- coding: utf-8 -*-

   # json_str = json.dumps(config)   #to json structure
    # python_str = json.loads(json_str)   #to python structure

from __future__ import unicode_literals
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

def readJson():
    with open('config.json','r') as f:
        config = json.load(f)
    return config

def writeJson(config):
    with open('config.json','w') as f:
        json.dumps(config,f)


if __name__=='__main__':
    config = readJson()
    print config['db']['Name']