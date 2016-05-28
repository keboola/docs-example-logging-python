from pygelf import GelfTcpHandler
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
fields = {"_some": {"structured": "data"}}
logger.addHandler(GelfTcpHandler(host=os.getenv('KBC_LOGGER_ADDR'), port=os.getenv('KBC_LOGGER_PORT'), debug=False, **fields))
logging.critical('A sample emergency message')
