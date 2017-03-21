#  -*- coding:utf-8 -*-
import logging
import logging.config
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug("tar url: ")