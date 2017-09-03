import logging
import os
#import pygelf
import logging_gelf.handlers
import logging_gelf.formatters
import djehouty.libgelf.handlers
import time

time.sleep(1)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# remove default logging to stdout
logger.removeHandler(logger.handlers[0])

# dummy data
fields = {"_some": {"structured": "data"}}

# pygelf
# does not work until https://github.com/keeprocking/pygelf/commit/348de66c1d06f40c5478af1635c1fd0e68edfa56 is resolved
#pygelf_handler = pygelf.GelfTcpHandler(host=os.getenv('KBC_LOGGER_ADDR'), port=os.getenv('KBC_LOGGER_PORT'), debug=False, **fields)
#logger.addHandler(pygelf_handler)
#logging.info('A sample info message (pygelf)')
#logging.warning('A sample warn message (pygelf)')
#logging.critical('A sample emergency message (pygelf)')
#
#logger.removeHandler(pygelf_handler)

# djehouty
djehouty_handler = djehouty.libgelf.handlers.GELFTCPSocketHandler(host=os.getenv('KBC_LOGGER_ADDR'), port=os.getenv('KBC_LOGGER_PORT'), static_fields=fields)
logger.addHandler(djehouty_handler)
logging.info('A sample info message (djehouty)')
logging.warning('A sample warn message (djehouty)')
logging.critical('A sample emergency message (djehouty)')

logger.removeHandler(djehouty_handler)

# logging_gelf
logging_gelf_handler = logging_gelf.handlers.GELFTCPSocketHandler(host=os.getenv('KBC_LOGGER_ADDR'), port=int(os.getenv('KBC_LOGGER_PORT')))
logging_gelf_handler.setFormatter(logging_gelf.formatters.GELFFormatter(null_character=True))
logger.addHandler(logging_gelf_handler)
logging.info('A sample info message (logging_gelf)')
logging.warning('A sample warn message (logging_gelf)')
logging.critical('A sample emergency message (logging_gelf)')

logger.removeHandler(logging_gelf_handler)

# incorrect logging_gelf
logging_gelf_handler = logging_gelf.handlers.GELFTCPSocketHandler(host=os.getenv('KBC_LOGGER_ADDR'), port=int(os.getenv('KBC_LOGGER_PORT')))
#logging_gelf_handler.setFormatter(logging_gelf.formatters.GELFFormatter(null_character=True))
logger.addHandler(logging_gelf_handler)
logging.info('A sample info message (invalid)')
logging.warning('A sample warn message (invalid)')
logging.critical('A sample emergency message (invalid)')

logger.removeHandler(logging_gelf_handler)
