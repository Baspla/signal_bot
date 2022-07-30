import logging

import requests

from util.constants import HOSTNAME, TELNUMBER, PROTOCOL, TEST_MODE

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
        results = [
            {"envelope": {
                "source": "+49...10",
                "sourceNumber": "+49...10",
                "sourceUuid": "3d89...ea65",
                "sourceName": "Tim Morgner",
                "sourceDevice": 2,
                "timestamp": 1659040118192,
                "dataMessage": {
                    "timestamp": 1659040118192,
                    "message": "/ping",
                    "expiresInSeconds": 0,
                    "viewOnce": False
                }
            }, "account": "+49...25"}]
        logger.debug("Fetched update: %s", results)
        return results;
