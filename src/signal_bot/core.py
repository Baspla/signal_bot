"""import functools"""
import logging
import time
from datetime import timedelta
from decorator_manager.message_manager import MessageManager
from signal_io.receiver import receiveData
from util.constants import POLLING_INTERVAL, LOGGING_LEVEL, printAllConstants
from util.envelope_utils import getSourceInformation
from timeloop import Timeloop
# Add new Handlers here
# noinspection PyUnresolvedReferences
from handler import ping, translate

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


def registerManager(manager):
    logger.info("Registered Decorator Manager %s", manager)
    update_decorators.append(manager)


#
# Core variables
#
update_decorators = list()


# noinspection PyUnresolvedReferences
def main():
    # logging.FileHandler("../log/signalBot.log", 'a', 'utf-8'),
    logging.basicConfig(handlers=[logging.StreamHandler()],
                        level=LOGGING_LEVEL)
    printAllConstants()

    # Register Decorators
    registerManager(MessageManager())

    # Start Core Loop
    tl = Timeloop()
    logging.getLogger("timeloop").setLevel(logging.CRITICAL)
    logger.info("Polling every %i seconds", POLLING_INTERVAL)

    @tl.job(interval=timedelta(seconds=POLLING_INTERVAL))
    def receive_polling():
        logger.debug("Fetching updates")
        results = receiveData()
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
