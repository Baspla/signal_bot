from abc import abstractmethod, ABC


class UpdateDecorator(ABC):
    @abstractmethod
    def process_update(self, source_information, data_message):
        pass

    @abstractmethod
    def check_update(self, source_information, data_message):
        pass
