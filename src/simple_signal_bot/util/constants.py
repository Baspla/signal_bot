import logging
import os

_logger = logging.getLogger("constants")

HOSTNAME = os.environ.get('SIGNAL_HOST', "localhost")

TELNUMBER = os.environ.get('SIGNAL_NUMBER')
if TELNUMBER is None:
    raise SystemExit("Missing SIGNAL_NUMBER")

POLLING_INTERVAL = int(os.environ.get('SIGNAL_INTERVAL', "15"))

PROTOCOL = os.environ.get('SIGNAL_PROTOCOL', "https")

TEST_MODE = os.environ.get('SIGNAL_TEST')
if TEST_MODE is None:
    TEST_MODE = False
elif TEST_MODE.lower() is "false":
    TEST_MODE = False
else:
    TEST_MODE = True

TEST_DATA = os.environ.get('SIGNAL_TESTDATA', "[]")


def printAllConstants():
    _logger.info("Config: SIGNAL_HOST = %s, SIGNAL_NUMBER = %s, SIGNAL_PROTOCOL = %s,"
                 " SIGNAL_INTERVAL = %s, SIGNAL_TEST = %s, SIGNAL_TESTDATA = %s", HOSTNAME, TELNUMBER, PROTOCOL,
                 POLLING_INTERVAL, TEST_MODE,TEST_DATA)
