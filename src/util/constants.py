import logging
import os

_logger = logging.getLogger("constants")

HOSTNAME = os.environ.get('SIGNAL_HOST', "localhost")

TELNUMBER = os.environ.get('SIGNAL_NUMBER')
if TELNUMBER is None:
    raise SystemExit("Missing SIGNAL_NUMBER")

POLLING_INTERVAL = int(os.environ.get('POLLING_INTERVAL', "15"))

LOGGING_LEVEL = os.environ.get('LOG_LEVEL', "INFO")

PROTOCOL = os.environ.get('SIGNAL_PROTOCOL', "https")

def printAllConstants():
    _logger.info("Config: SIGNAL_HOST = %s, SIGNAL_NUMBER = %s, SIGNAL_PROTOCOL = %s,"
                 " POLLING_INTERVAL = %s, LOG_LEVEL = %s",HOSTNAME,TELNUMBER,PROTOCOL,POLLING_INTERVAL,LOGGING_LEVEL)
