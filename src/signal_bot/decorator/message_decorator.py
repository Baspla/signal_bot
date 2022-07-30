import logging

from decorator_manager.message_manager import messageHandlers
from model.update_handler import UpdateHandler

logger = logging.getLogger("MessageDecorator")


class MessageHandler(UpdateHandler):
    def __init__(self, callback, regex):
        super().__init__(callback)
        self.regex = regex


# Message Decorator
class Message:
    def __init__(self, regex=".*"):
        self.regex = regex

    def __call__(self, function):
        handler = MessageHandler(function, self.regex)
        messageHandlers.append(handler)
        print("Hooked a ContextMessageHandler", handler)
        return function
