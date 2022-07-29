import logging

from decorator.message import Message
from signal_cli.sender import sendText

from util.group_utils import groupContextFromId

logger = logging.getLogger("ping")


@Message(regex="^/ping$")
def test3(source_information, data_message, message):
    if "groupInfo" in data_message:
        internal = data_message["groupInfo"]["groupId"]
        group_context = groupContextFromId(internal)
        sendText(group_context, "Pong!")
    else:
        sendText(source_information.source_uuid, "Pong!")
