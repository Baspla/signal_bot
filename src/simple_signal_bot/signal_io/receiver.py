import json
import logging

import requests

from simple_signal_bot.util.constants import HOSTNAME, TELNUMBER, PROTOCOL, TEST_MODE, TEST_DATA

logger = logging.getLogger("receiver")


def receiveData():
    results = []
    try:
        uri = f"{PROTOCOL}://{HOSTNAME}/v1/receive/{TELNUMBER}"
        logger.debug("Fetching Signal-CLI updates from %s", uri)
        response = requests.get(uri, timeout=120)
        logger.debug("Parsing JSON Response")
        results = response.json()
        logger.debug("Fetched update: %s", results)
    except ValueError as vexc:
        logger.error("ValueError: %s", vexc)
    except requests.exceptions.RequestException as e:
        logger.error("RequestException: %s", e)

    return results


if TEST_MODE:
    logger.info("Overriding recieveData with Test Data")


    def receiveData():
        logger.info("This is Test Data")
        try:
            results = json.loads(TEST_DATA)
            logger.debug("Fetched update: %s", results)
        except json.decoder.JSONDecodeError as jse:
            logger.error("Test Data JSONDecodeError: %s", jse)
            return []
        return results
