"""import functools"""
import logging
import time
from datetime import timedelta
from decorator.message import MessageDecorator
from decorator.context_message import ContextMessageDecorator
from signal_cli.receiver import signalPolling
from util.constants import POLLING_INTERVAL, LOGGING_LEVEL
from util.envelope_utils import getSourceInformation
from timeloop import Timeloop

logger = logging.getLogger("core")


def process_envelope(envelope):
    source_information = getSourceInformation(envelope)
    if "dataMessage" in envelope:
        data_message = envelope["dataMessage"]
        for x in range(len(update_decorators)):
            if update_decorators[x].check_update(source_information, data_message):
                update_decorators[x].process_update(source_information, data_message)
    else:  # Updates ohne dataMessage sind sync/call/receipt/typing und werden daher ignoriert
        pass


def registerDecorator(update_decorator):
    logger.info("Registered UpdateDecorator %s", update_decorator)
    update_decorators.append(update_decorator)


#
# Core variables
#

polling_function = signalPolling
update_decorators = list()


# noinspection PyUnresolvedReferences
def main():

    logging.basicConfig(handlers=[logging.FileHandler("../log/signalBot.log",'a', 'utf-8'), logging.StreamHandler()],
                        level=LOGGING_LEVEL)

    # Register Decorators # Add new Decorators here
    registerDecorator(MessageDecorator())
    registerDecorator(ContextMessageDecorator())

    import handler.ping
    import handler.translate

    # Start Core Loop
    tl = Timeloop()
    logging.getLogger("timeloop").setLevel(logging.CRITICAL)
    logger.info("Polling every %i seconds",POLLING_INTERVAL)
    @tl.job(interval=timedelta(seconds=POLLING_INTERVAL))
    def receive_polling():
        logger.debug("Fetching updates")
        results = polling_function()
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


if __name__ == '__main__':
    main()
