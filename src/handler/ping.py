import logging

from decorator.context_message import ContextMessage
from signal_cli.sender import sendText

logger = logging.getLogger("ping")


@ContextMessage(regex="^/ping$")
def ping(source_information, data_message,context, message):
    sendText(context, "Pong!")
