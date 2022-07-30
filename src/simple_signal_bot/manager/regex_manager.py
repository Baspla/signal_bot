import logging

from simple_signal_bot.util.context import getOptionalGroupContext
from simple_signal_bot.util.regex import regexCheck

logger = logging.getLogger("RegexManager")


class RegexHandler:
    def __init__(self, callback, regex):
        self.callback=callback
        self.regex = regex


class RegexManager:
    def __init__(self):
        self.regex_handlers = list()
        pass

    def register_handler(self,regex_handler):
        self.regex_handlers.append(regex_handler)

    def process_update(self, source_information, data_message):
        logger.debug("Processing update")
        if "message" in data_message:
            msg = data_message["message"]
            if msg is not None:
                for x in range(len(self.regex_handlers)):
                    handler = self.regex_handlers[x]
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

    @staticmethod
    def check_update(source_information, data_message):
        if "message" in data_message:
            logger.debug("Handler check passed")
            msg = data_message["message"]
            return msg is not None
        return False
