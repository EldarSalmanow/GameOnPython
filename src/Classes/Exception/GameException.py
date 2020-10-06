from abc import abstractmethod


class GameException(Exception):
    @abstractmethod
    def __init__(self, message):
        pass

    @abstractmethod
    def printError(self):
        pass
