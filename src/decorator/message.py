import logging
import re

from model.update_decorator import UpdateDecorator
from model.update_handler import UpdateHandler

logger = logging.getLogger("messageDecorator")
messageHandlers = list()


class MessageHandler(UpdateHandler):
    def __init__(self, callback, regex):
        super().__init__(callback)
        self.regex = regex


class MessageDecorator(UpdateDecorator):
    def __init__(self):
        pass

    def process_update(self, source_information, data_message):
        logger.debug("Processing update")
        if "message" in data_message:
            msg = data_message["message"]
            if msg is not None:
                for x in range(len(messageHandlers)):
                    handler = messageHandlers[x]
                    if isinstance(handler, MessageHandler):  # Möglicherweise überflüssig
                        logger.debug("Using RegEx %s on message %s", handler.regex, msg)
                        try:
                            pattern = re.compile(handler.regex)
                            if pattern.match(msg):
                                logger.debug("Handler %s matched RegEx: %s", handler, handler.regex)
                                handler.callback(source_information, data_message, msg)
                        except re.error:
                            logger.error("Invalid RegEx: %s", messageHandlers[x].regex)
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


# Decorator
class Message:
    def __init__(self, regex=".*"):
        self.regex = regex

    def __call__(self, function):
        handler = MessageHandler(function, self.regex)
        messageHandlers.append(handler)
        logger.debug("Registered MessageHandler %s", handler)
        return function
