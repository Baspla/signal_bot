import logging

from model.update_decorator import UpdateDecorator
from model.update_handler import UpdateHandler
from util.context import getOptionalGroupContext
from util.regex import regexCheck

logger = logging.getLogger("ContextMessageDecorator")
handlers = list()


class ContextMessageHandler(UpdateHandler):
    def __init__(self, callback, regex):
        super().__init__(callback)
        self.regex = regex


class ContextMessageDecorator(UpdateDecorator):
    def __init__(self):
        pass

    def process_update(self, source_information, data_message):
        logger.debug("Processing update")
        if "message" in data_message:
            msg = data_message["message"]
            if msg is not None:
                for x in range(len(handlers)):
                    handler = handlers[x]
                    if isinstance(handler, ContextMessageHandler):  # Möglicherweise überflüssig
                        if regexCheck(handler.regex, msg):
                            context = getOptionalGroupContext(data_message)
                            if context is None:
                                context = source_information.source_uuid
                            handler.callback(source_information, data_message, context, msg)
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


# Besserer Message Decorator der den richtigen Antwort Context ermittelt
class ContextMessage:
    def __init__(self, regex=".*"):
        self.regex = regex

    def __call__(self, function):
        handler = ContextMessageHandler(function, self.regex)
        handlers.append(handler)
        logger.debug("Registered ContextMessageHandler %s", handler)
        return function
