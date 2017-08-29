import logging
import os
import pygelf
import graypy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# remove default logging to stdout
logger.removeHandler(logger.handlers[0])

# dummy data
fields = {"_some": {"structured": "data"}}

# pygelf
pygelf_handler = pygelf.GelfUdpHandler(host=os.getenv('KBC_LOGGER_ADDR'), port=os.getenv('KBC_LOGGER_PORT'), debug=False, **fields)
logger.addHandler(pygelf_handler)
logging.info('A sample info message (pygelf)')
logging.warning('A sample warn message (pygelf)')
logging.critical('A sample emergency message (pygelf)')

logger.removeHandler(pygelf_handler)

# graypy
graypy_handler = graypy.GELFHandler(host=os.getenv('KBC_LOGGER_ADDR'), port=int(os.getenv('KBC_LOGGER_PORT')), extra_fields=fields)
logger.addHandler(graypy_handler)
logging.info('A sample info message (graypy)')
logging.warning('A sample warn message (graypy)')
logging.critical('A sample emergency message (graypy)')

logger.removeHandler(logging_gelf_handler)
