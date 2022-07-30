import logging
import time
from datetime import timedelta
from timeloop import Timeloop

from simple_signal_bot.decorator.command_decorator import CommandDecorator
from simple_signal_bot.decorator.message_decorator import MessageDecorator
from simple_signal_bot.manager.regex_manager import RegexManager
from simple_signal_bot.signal_io.receiver import receiveData
from simple_signal_bot.signal_io.sender import Sender
from simple_signal_bot.util.constants import POLLING_INTERVAL, printAllConstants
from simple_signal_bot.util.envelope_utils import getSourceInformation


class SignalBot:

    def __init__(self):
        self.update_decorators = list()
        self.logger = logging.getLogger("core")
        regex_manager = RegexManager()
        self.__registerManager(regex_manager)
        self.Message = MessageDecorator(regex_manager).decorator_factory
        self.Command = CommandDecorator(regex_manager).decorator_factory
        self.sender = Sender()

    def __process_envelope(self, envelope):
        source_information = getSourceInformation(envelope)
        if "dataMessage" in envelope:
            data_message = envelope["dataMessage"]
            for x in range(len(self.update_decorators)):
                if self.update_decorators[x].check_update(source_information, data_message):
                    self.update_decorators[x].process_update(source_information, data_message)
        else:  # Updates ohne dataMessage sind sync/call/receipt/typing und werden daher ignoriert
            pass

    def __registerManager(self, manager):
        self.logger.info("Registered Decorator Manager %s", manager)
        self.update_decorators.append(manager)

    def run(self):
        printAllConstants()

        # Start Core Loop
        tl = Timeloop()
        logging.getLogger("timeloop").setLevel(logging.CRITICAL)
        self.logger.info("Polling every %i seconds", POLLING_INTERVAL)

        @tl.job(interval=timedelta(seconds=POLLING_INTERVAL))
        def receive_polling():
            self.logger.debug("Fetching updates")
            results = receiveData()
            for x in range(len(results)):
                delivery = results[x]
                if "envelope" in delivery:
                    envelope = delivery["envelope"]
                    self.__process_envelope(envelope)
            return False

        tl.start()

        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                tl.stop()
                break
