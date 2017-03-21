#  -*- coding:utf-8 -*-
import logging
import logging.config
import json
import demjson
import urllib
import httplib
import copy
import guiserver 

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

from flask import Flask,jsonify,abort,make_response,request,url_for
from flask.ext.restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

kipp_status={
	"online":"online",
	"ready":"ready",
	"running":"running",
	"error":"error",
	"offline":"offline"
}

def start(kipp_body,conf):

	try:

		logger.debug("send message to tars!");
	
 		hello_params = json.JSONEncoder().encode(kipp_body) 
	 	tarurl="/hello"
	 	

	 	logger.debug("say hello data:")
	 	

	 	hellostr=sentPost(tarurl,hello_params)

	 	logger.debug("start say hello res type is :")
	 
	 	logger.debug(type(hellostr))
	 	decode_str = json.loads(hellostr)
	 	kipp_body['timestamp']=decode_str['timestamp']

	 	logger.debug("add new timestamp in kipp_body")
	 	logger.debug(kipp_body)

	 	addkipp_url="/kippstatus"

	 	res_status=sentPost(addkipp_url,hello_params)
	 	logger.debug("tars status res is :")
	 	
	 	logger.debug(res_status)
	 	# if(rep_status['restult']=="false"):

	    #如果kipp已经存在更新状态为 online 目前暂不实现

 		return True
 	except Exception ,e :
	
		logger.error('exception',e.message) 
		return False


	#add kipps



	#if fail update status


# def prepare ():

# 	#read conf file

# 	#set kippbody




def conf_body(conf): 
	print conf['body']['name']
	kipp={
	    "name":conf['body']['name'],
	    "type":conf['body']['type'],
	    "status":kipp_status['online'],
	    "timestamp":"",
	    "ip":conf['host']['ip'],
	    "port":conf['host']['port'],
	    "sid":conf['body']['sid']
	}
	return kipp

def load_conf():
	f=open("config.json")
	s=json.load(f)
	#o=demjson.encode(s)
	
	f.close
	return s
def sentPost(url,params):
	httpClient = None
	try:
	    headers = {"Content-type": "application/json"
	                    , "Accept": "text/plain"}
	 
	    httpClient = httplib.HTTPConnection("localhost", 7988, timeout=30)
	    httpClient.request("POST", url, params, headers)
	 
	    response = httpClient.getresponse()
	    # print response.status
	    # print response.reason
	    # print response.read()
	    # print response.getheaders() #获取头信息
	    result=response.read()
	except Exception, e:
	    print e
	finally:
	    if httpClient:
	        httpClient.close()
	return result

@app.route('/task', methods=['POST'])
def create_task():
	app.logger.debug("receive tars message:")
	app.logger.debug(request.json)
	result=guiserver.run(request.json)

 	return jsonify(result),201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    
    
    conf=load_conf()
    kipp_body=conf_body(conf)
    start(kipp_body,conf)
    app.run(debug=True)

