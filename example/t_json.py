#encoding:utf-8
import json
import demjson

def load():
	f=open("tt.json");
	s=json.load(f)
	o=demjson.encode(s)
	#print o.body.name
	print s
	print s['body']['name']
	print type(s['body'])
	s['name']='a123'
	s['bb']='rjrj'
	s['cc']='sdf'
	s['aa']='df'
	f.close
	for str in s:
		print str,s[str]

	

	st={"result":"success",
	"answer":"I'm TARS your time is:Thu Feb 02 2017 10:38:55 GMT+0800 (CST)",
	"timestamp":1486003135229,
	"sid":"tars_1486003135229_39"}

	print type(st)
	print st['timestamp']

	data1 = {'b': 789, 'c': 456, 'a': 123}
	encode_json = json.dumps(st)
	print type(encode_json), encode_json

	decode_json = json.loads(encode_json)
	print type(decode_json)
	print decode_json['result']
	print decode_json
	decode_json['abc']='uccess11232'
	print decode_json
	decode_json['result']='2342342'
	print decode_json
	return o
a=load();
print a

