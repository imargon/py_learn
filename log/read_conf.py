#encoding:utf-8

import os,sys
import codecs

print os.getcwd()

file_object = open("D:\py\log\kreminder.conf","r")
#type = sys.getfilesystemencoding()
#file_object.seek(200)
#print file_object.readline()
#print(file_object.read()).decode('utf-8').encode(type)
#print(file_object.read()).decode(type).encode('utf-8')

def parse_conf_file(file_object):
    status = 0  # 状态机： 0 - 初始状态， 1 - 读取休息提醒配置， 2 - 读取代办事项配置
    remind_rest_dict = {}
    todo_list_dict = {}
    file_content = [ line.strip() for line in file_object.readlines() ]
    #print file_content
    for line in file_content:
        #print line
        if len(line) == 0 or line[0] == "#":
            continue
        elif line == "[REST_INTERVAL]":
            status = 1
            continue
        elif line == "[TODO_LIST]":
            status = 2
            continue
        else:
            if line.count("=") != 1:
                continue
            else:
                key, val = [ item.strip(' "') for item in line.split("=") ]
                print 'key=',key ,'val=',val
                if status == 1:
                    if not cmp(key, "interval"):
                        remind_rest_dict["interval"] = int(val)
                    elif not cmp(key, "message"):
                        remind_rest_dict["message"] = unicode(val, "utf-8")
                    else:
                        print(key + " 是未定义的配置项.", "error")
                elif status == 2:
                    todo_list_dict[key] = unicode(val, "utf-8")
                else:
                    print("在解析配置文件时出现未定义的状态： " + str(status), "error")

    return remind_rest_dict, todo_list_dict

parse_conf_file(file_object)