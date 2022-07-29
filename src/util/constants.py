import logging
import os

HOSTNAME = os.environ.get('SIGNAL_HOST', "localhost")

TELNUMBER = os.environ.get('SIGNAL_NUMBER')
if TELNUMBER is None:
    raise SystemExit("Missing SIGNAL_NUMBER")

POLLING_INTERVAL = int(os.environ.get('POLLING_INTERVAL', "15"))

LOGGING_LEVEL = os.environ.get('LOG_LEVEL', "INFO")
