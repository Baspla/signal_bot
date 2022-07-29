import logging

import requests

from util.constants import TELNUMBER, HOSTNAME

logger = logging.getLogger("sender")


def sendText(recepient, message):
    body = {
        "message": f"{message}",
        "number": f"{TELNUMBER}",
        "recipients": [
            f"{recepient}"
        ]
    }
    logger.debug("Sent message '%s' to %s", message, recepient)
    postResponse = requests.post(f"https://{HOSTNAME}/v2/send", json=body)
    logger.debug("Response: %s", postResponse)
