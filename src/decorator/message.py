import logging
import re

from model.update_decorator import UpdateDecorator
from model.update_handler import UpdateHandler

messageHandlers = list()
logger = logging.getLogger("messageDecorator")


class MessageHandler(UpdateHandler):
    def __init__(self, callback, regex):
        super().__init__(callback)
        self.regex = regex


class MessageDecorator(UpdateDecorator):

    def process_update(self, source_information, data_message):
        for x in range(len(messageHandlers)):
            handler = messageHandlers[x]
            if "message" in data_message:
                message = data_message["message"]
                if message is not None:
                    if isinstance(handler, MessageHandler):
                        logger.debug("Using RegEx: %s", handler.regex)
                        try:
                            pattern = re.compile(handler.regex)
                            if pattern.match(message):
                                handler.callback(source_information, data_message, message)
                        except re.error:
                            logger.error("Invalid RegEx: %s", messageHandlers[x].regex)

    def check_update(self, source_information, data_message):
        if "message" in data_message:
            logger.debug("Check passed ✔️")
            msg = data_message["message"]
            return msg is not None
        return False


# Decorator
def message(_func=None, *, regex=".*"):
    def decorator_every(func):
        handler = MessageHandler(func, regex)
        messageHandlers.append(handler)
        logger.debug("Registered MessageHandler %s",handler)
        return func

    if _func is None:
        return decorator_every
    else:
        return decorator_every(_func)
