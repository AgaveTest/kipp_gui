#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py

import urllib
import urllib2
import json
    
def http_post():
    url='http://127.0.0.1:7988/kippstatus'
    values = {"ip":"127.0.0.1","name":"guikipp001","port":"5000","sid":"guikipp001","status":"online","timestamp":"","type":"gui"}
    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()                    # 获取服务器返回的页面信息

resp = http_post()
print resp