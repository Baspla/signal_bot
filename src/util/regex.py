import logging
import re

logger = logging.getLogger("regex")


def regexCheck(regex, msg):
    logger.debug("Using RegEx %s on message %s", regex, msg)
    try:
        pattern = re.compile(regex)
        success = pattern.match(msg)
        logger.debug("RegEx returned %s", success)
        return success

    except re.error:
        logger.error("Invalid RegEx: %s", regex)
    return False
