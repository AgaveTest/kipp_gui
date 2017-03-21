#!/usr/bin/env python
#coding=utf8
 
import httplib, urllib,json
 
httpClient = None
try:
    params = json.JSONEncoder().encode({"ip":"127.0.0.1",
                "name":"guikipp001",
                "port":"5000",
                "sid":"guikipp001",
                "status":"online","timestamp":"","type":"gui"})  

    headers = {"Content-type": "application/json"
                    , "Accept": "text/plain"}
 
    httpClient = httplib.HTTPConnection("localhost", 7988, timeout=30)
    httpClient.request("POST", "/kippstatus", params, headers)
 
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()