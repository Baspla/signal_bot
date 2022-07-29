"""import functools"""
import base64
import os
import re
import time
import requests
from timeloop import Timeloop
from datetime import timedelta

HOSTNAME = os.environ.get('SIGNAL_HOST')
if HOSTNAME is None:
    HOSTNAME = "localhost"
TELNUMBER = os.environ.get('SIGNAL_NUMBER')
if TELNUMBER is None:
    raise SystemExit("Missing SIGNAL_NUMBER")


class SourceInformation:
    def __init__(self, source_uuid, source_number, source_name, source_device):
        self.source_uuid=source_uuid
        self.source_number=source_number
        self.source_name=source_name
        self.source_device=source_device

class UpdateHandler:
    def __init__(self):
        pass


class MessageHandler(UpdateHandler):
    def __init__(self, regex, callback):
        super().__init__()
        self.regex = regex
        self.callback = callback


messageHandlers = list()


def signal_message(_func=None, *, regex=".*"):
    def decorator_every(func):
        messageHandlers.append(MessageHandler(regex, func))
        return func

    if _func is None:
        return decorator_every
    else:
        return decorator_every(_func)


@signal_message()
def test1(source_information,data_message,message):
    print(f"Nachricht {message}")


@signal_message(regex="^([A-Z][0-9]+)+$")
def test2(source_information,data_message,message):
    print("Buchstabe/Zahl abwechselnd")


def encodeGroupId(group_id): #Sollte diese Methode nicht mehr gehen so muss über v1/groups die id abgeglichen werden
    return f"group.{base64.b64encode(group_id.encode('ascii')).decode('ascii')}"


@signal_message(regex="/ping")
def test3(source_information,data_message,message):
    if "groupInfo" in data_message:
        print(f'{data_message["groupInfo"]["groupId"]} encoded to {encodeGroupId(data_message["groupInfo"]["groupId"])}')
        sendText(encodeGroupId(data_message["groupInfo"]["groupId"]), "Pong!")
    else:
        sendText(source_information.source_uuid, "Pong!")


tl = Timeloop()


def process_data_message(source_information,data_message):
    for x in range(len(messageHandlers)):
        handler = messageHandlers[x]
        if "message" in data_message:
            message = data_message["message"]
            if message is not None:
                if isinstance(handler, MessageHandler):
                    try:
                        pattern = re.compile(handler.regex)
                        if pattern.match(message):
                            handler.callback(source_information,data_message,message)
                    except re.error:
                        print("ERROR Ungültiges Regex:")
                        print(messageHandlers[x].regex)


def process_sync_message(source_information,sync_message):
    print("Sync Message ignoriert")
    pass


def process_call_message(source_information,call_message):
    print("Call Message ignoriert")
    pass


def process_receipt_message(source_information,receipt_message):
    print("Receipt Message ignoriert")
    pass


def process_typing_message(source_information,typing_message):
    print("Receipt Message ignoriert")
    pass


def process_envelope(envelope):
    source = SourceInformation(envelope["sourceUuid"],envelope["sourceNumber"],envelope["sourceName"],envelope["sourceDevice"])
    if "dataMessage" in envelope:
        process_data_message(source,envelope["dataMessage"])
    if "syncMessage" in envelope:
        process_sync_message(source,envelope)
    if "callMessage" in envelope:
        process_call_message(source,envelope)
    if "receiptMessage" in envelope:
        process_receipt_message(source,envelope)
    if "typingMessage" in envelope:
        process_typing_message(source,envelope)


def sendText(recepient,message):
    body = {
      "message": f"{message}",
      "number": f"{TELNUMBER}",
      "recipients": [
        f"{recepient}"
      ]
    }
    print(body)
    postResponse = requests.post(f"https://{HOSTNAME}/v2/send", json=body)


@tl.job(interval=timedelta(seconds=15))
def receive_polling():
    results = []
    try:
        print("fetching updates...")
        response = requests.get(f"https://{HOSTNAME}/v1/receive/{TELNUMBER}")
        results = response.json()
        print(f"fetched update: {results}")
    except ValueError as vexc:
        print(f"ValueError: {vexc}")
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")

    for x in range(len(results)):
        delivery = results[x]
        if "envelope" in delivery:
            envelope = delivery["envelope"]
            process_envelope(envelope)

    return False


tl.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        tl.stop()
        break
