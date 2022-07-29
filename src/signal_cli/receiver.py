import logging

import requests

from util.constants import HOSTNAME, TELNUMBER


logger = logging.getLogger("receiver")


def signalPolling():
    results = []
    try:
        logger.debug("Fetching Signal-CLI updates")
        response = requests.get(f"{PROTOCOL}://{HOSTNAME}/v1/receive/{TELNUMBER}")
        results = response.json()
        logger.debug("Fetched update: %s", results)
    except ValueError as vexc:
        logger.error("ValueError: %s", vexc)
    except requests.exceptions.RequestException as e:
        logger.error("RequestException: %s", e)

    return results
