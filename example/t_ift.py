#  -*- coding:utf-8 -*-


def abc():
	res=None

	if res is None:
		print "in abc"
		res="123"
	else:
		print "in abc;"

	if res is None:
		print "in two"
	else:
		print "in else"


abc();