"""import functools"""
import re

MessageHandlers = list()


class MessageHandler:
    def __init__(self, regex, callback):
        self.regex = regex
        self.callback = callback


def signal_message(_func=None, *, regex=".*"):
    def decorator_every(func):
        MessageHandlers.append(MessageHandler(regex, func))
        return func

    if _func is None:
        return decorator_every
    else:
        return decorator_every(_func)


@signal_message()
def test1():
    print("HEY 1")


@signal_message(regex="^([A-Z][0-9]+)+$")
def test2():
    print("HEY 2")


@signal_message(regex="A")
def test3():
    print("HEY 3")


message = "R2D2"


for x in range(len(MessageHandlers)):
    try:
        pattern = re.compile(MessageHandlers[x].regex)
        if pattern.match(message):
            MessageHandlers[x].callback()
    except re.error:
        print("ERROR Ungültiges Regex:")
        print(MessageHandlers[x].regex)
