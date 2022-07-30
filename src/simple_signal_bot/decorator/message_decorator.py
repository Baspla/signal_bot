import logging

from simple_signal_bot.manager.regex_manager import RegexHandler

logger = logging.getLogger("MessageDecorator")


class MessageDecorator:

    def __init__(self, regex_manager):
        self.regex_manager = regex_manager
        pass

    def decorator_factory(self, regex=".*"):
        def decorator(function):
            handler = RegexHandler(function, regex)
            self.regex_manager.register_handler(handler)
            logger.info("Hooked a MessageDecorator for %s", regex)
            return function

        return decorator
