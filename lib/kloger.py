#encoding:utf-8
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='kipp.log',
                filemode='w')
#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

# #################################################################################################
# #定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
# Rthandler = RotatingFileHandler('kipp.log', maxBytes=10*1024*1024,backupCount=5)
# Rthandler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# Rthandler.setFormatter(formatter)
# logging.getLogger('').addHandler(Rthandler)
# ################################################################################################


# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

def debug(s):
	this.logging.debug(s)

def info(s):
	this.logging.info(s)

def warning(s):
	this.logging.warning(s)  