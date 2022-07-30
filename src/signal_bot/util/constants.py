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

TEST_MODE = os.environ.get('TEST_MODE')
if TEST_MODE is None:
    TEST_MODE = False
elif TEST_MODE.lower() is "false":
    TEST_MODE = False
else:
    TEST_MODE = True


def printAllConstants():
    _logger.info("Config: SIGNAL_HOST = %s, SIGNAL_NUMBER = %s, SIGNAL_PROTOCOL = %s,"
                 " POLLING_INTERVAL = %s, LOG_LEVEL = %s, TEST_MODE = %s", HOSTNAME, TELNUMBER, PROTOCOL,
                 POLLING_INTERVAL, LOGGING_LEVEL, TEST_MODE)
