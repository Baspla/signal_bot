import logging

import requests

from util.constants import TELNUMBER, HOSTNAME, PROTOCOL

logger = logging.getLogger("sender")


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
    logger.debug("Sending message via %s", uri)
    post_response = requests.post(uri, json=body,timeout=60)
    logger.debug("Response: %s", post_response)