import logging

from simple_signal_bot.manager.regex_manager import RegexHandler

logger = logging.getLogger("CommandDecorator")


class CommandDecorator:

    def __init__(self,regex_manager):
        self.regex_manager = regex_manager
        pass

    def decorator_factory(self, cmd=None):
        def decorator(function):
            def newfunc(source_information, data_message, context, message):
                args = str(message).split(" ")
                function(source_information, data_message, context, message, args)
            regex = f"^/{cmd}\\s*"
            if cmd is None:
                regex = f"^/{function.__name__}\\s*"
            handler = RegexHandler(newfunc, regex)
            self.regex_manager.register_handler(handler)
            logger.info("Hooked a CommandDecorator for %s", regex)
            return newfunc

        return decorator
