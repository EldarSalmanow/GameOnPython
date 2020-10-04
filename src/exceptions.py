from abc import abstractmethod


class GameException(Exception):
    @abstractmethod
    def __init__(self, message):
        pass

    @abstractmethod
    def printError(self):
        pass


class GameTypeException(GameException):
    def __init__(self, message):
        self.__typeError = "GameTypeException"
        self.__message = message

    def printError(self):
        print(self.__typeError + ": " + self.__message)
