
# -*- encoding: utf-8 -*-
'''
@File    : time.py
@Author  : vgzx
@Date    : 2020/08/13 22:54
@Contact : viewgrand@163.com
@Desc    : 时间相关的一些工具方法

'''

import time



#fun_desc: %Y/%m/%d %H:%M -> 时间戳
#@param  : string
#@return : int
def unixtime(timestring):
    timeArray = time.strptime(timestring, "%Y/%m/%d %H:%M")
    return int(time.mktime(timeArray))


#fun_desc: 时间戳 -> %Y/%m/%d %H:%M
#@param  : string
#@return : int
def localtime(unixtime):
    timeArray = time.localtime(unixtime)
    timestring = time.strftime("%Y/%m/%d %H:%M", timeArray)
    return timestring


