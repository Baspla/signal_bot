import logging

import requests

from util.constants import TELNUMBER, HOSTNAME, PROTOCOL, TEST_MODE

logger = logging.getLogger("sender")


def post(uri, body):
    logger.debug("Sending message via %s", uri)
    post_response = requests.post(uri, json=body, timeout=60)
    logger.debug("Response: %s", post_response)


def sendText(recepient, message):
    body = {
        "message": f"{message}",
        "number": f"{TELNUMBER}",
        "recipients": [
            f"{recepient}"
        ]
    }
    uri = f"{PROTOCOL}://{HOSTNAME}/v2/send"
    logger.debug("Sending message '%s' to %s", message, recepient)
    post(uri, body)


if TEST_MODE:
    logger.info("Catching outgoing messages")


    def post(uri, body):
        logger.debug("Sending message via %s", uri)
        logger.info("Sending TEST uri: %s body: %s", uri, body)
        logger.debug("Response: %s", "Tis but a test")
