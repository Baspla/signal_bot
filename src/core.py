"""import functools"""
import logging
import time
from datetime import timedelta
from decorator.message import MessageDecorator
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
    logging.basicConfig(handlers=[logging.FileHandler("../log/signalBot.log"), logging.StreamHandler()],
                        level=LOGGING_LEVEL)

    # Register Decorators # Add new Decorators here
    registerDecorator(MessageDecorator())

    import handler.ping

    # Start Core Loop
    tl = Timeloop()

    @tl.job(interval=timedelta(seconds=POLLING_INTERVAL))
    def receive_polling():
        logger.info("Fetching updates")
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
