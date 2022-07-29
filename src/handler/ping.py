import logging

from decorator.message import message
from signal_cli.sender import sendText

from util.group_utils import encodeGroupId

logger = logging.getLogger("ping")


@message(regex="/ping")
def test3(source_information, data_message, message):
    if "groupInfo" in data_message:
        logger.info("Ping in group %s (enc: %s)",
                    {data_message["groupInfo"]["groupId"]},
                    {encodeGroupId(data_message["groupInfo"]["groupId"])})
        sendText(encodeGroupId(data_message["groupInfo"]["groupId"]), "Pong!")
    else:
        sendText(source_information.source_uuid, "Pong!")
