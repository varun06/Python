import logging
from logging import handlers

def config():
	logger = logging.getLogger('app')
	logger.setLevel(logging.ERROR)
	handler = handlers.RotatingFileHandler(
				'debug.log'
				maxBytes = (1024*1024)
				backupCount = 5
				)
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	logger.addHandler(handler)

	logger = logging.getLogger('app.othersub')
	logger.setLevel(logging.DEBUG)