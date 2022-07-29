import os

HOSTNAME = os.environ.get('SIGNAL_HOST')
if HOSTNAME is None:
    HOSTNAME = "localhost"

TELNUMBER = os.environ.get('SIGNAL_NUMBER')
if TELNUMBER is None:
    raise SystemExit("Missing SIGNAL_NUMBER")

POLLING_INTERVAL = os.environ.get('POLLING_INTERVAL')
if POLLING_INTERVAL is None:
    POLLING_INTERVAL = 15
else:
    POLLING_INTERVAL = int(POLLING_INTERVAL)
