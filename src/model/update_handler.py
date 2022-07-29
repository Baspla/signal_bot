from abc import ABC


class UpdateHandler(ABC):
    def __init__(self, callback):
        self.callback = callback
