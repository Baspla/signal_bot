import logging

from decorator.message_decorator import Message
from signal_io.sender import sendText

logger = logging.getLogger("ping")

class Ping:
    @Message(regex="^/ping$")
    def ping(source_information, data_message,context, message):
        sendText(context, "Pong!")
