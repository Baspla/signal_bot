from simple_signal_bot.util.group_utils import groupContextFromId


def getOptionalGroupContext(data_message):
    if "groupInfo" in data_message:
        internal = data_message["groupInfo"]["groupId"]
        return groupContextFromId(internal)
    return None
