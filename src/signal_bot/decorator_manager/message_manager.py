import logging

from model.update_decorator import UpdateDecorator
from util.context import getOptionalGroupContext
from util.regex import regexCheck

logger = logging.getLogger("MessageManager")

messageHandlers = list()


class MessageManager(UpdateDecorator):
    def __init__(self):
        pass

    def process_update(self, source_information, data_message):
        logger.debug("Processing update")
        if "message" in data_message:
            msg = data_message["message"]
            if msg is not None:
                for x in range(len(messageHandlers)):
                    handler = messageHandlers[x]
                    if regexCheck(handler.regex, msg):
                        logger.debug("Message '%s' fit '%s'", msg, handler.regex)
                        context = getOptionalGroupContext(data_message)
                        if context is None:
                            context = source_information.source_uuid
                        handler.callback(source_information, data_message, context, msg)
                    else:
                        logger.debug("Message '%s' didn't fit '%s'", msg, handler.regex)
            else:
                logger.debug("Empty message")
        else:
            logger.debug("Missing message")

    def check_update(self, source_information, data_message):
        if "message" in data_message:
            logger.debug("Check passed")
            msg = data_message["message"]
            return msg is not None
        return False
