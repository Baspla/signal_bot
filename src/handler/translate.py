import logging

from decorator.context_message import ContextMessage
from signal_cli.sender import sendText
from gpytranslate import Translator
from random import randint
import asyncio

logger = logging.getLogger("translate")

users = dict()


@ContextMessage()
def translate(source_information, data_message, context, message):
    async def translator():
        t = Translator()
        logger.debug("Von: %s", message)
        foerign1 = await t.translate(message, targetlang="it")
        logger.debug("Über: %s", foerign1.text)
        foerign2 = await t.translate(foerign1.text, targetlang="ru")
        logger.debug("Über: %s", foerign2.text)
        foerign3 = await t.translate(foerign1.text, targetlang="ja")
        logger.debug("Über: %s", foerign3.text)
        result = await t.translate(foerign2.text, targetlang="de")
        logger.debug("Zu: %s", result.text)
        # language = await t.detect(result.text)
        sendText(context, f"Meintest du: {result.text}")
        pass

    if randint(0, 99) < 1:
        asyncio.run(translator())
