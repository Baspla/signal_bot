import logging

import requests

from util.constants import HOSTNAME, TELNUMBER, PROTOCOL

logger = logging.getLogger("receiver")


def signalPolling():
    results = []
    try:
        uri = f"{PROTOCOL}://{HOSTNAME}/v1/receive/{TELNUMBER}"
        logger.debug("Fetching Signal-CLI updates from %s",uri)
        response = requests.get(uri,timeout=120)
        logger.debug("Parsing JSON Response")
        results = response.json()
        logger.debug("Fetched update: %s", results)
    except ValueError as vexc:
        logger.error("ValueError: %s", vexc)
    except requests.exceptions.RequestException as e:
        logger.error("RequestException: %s", e)

    return results
