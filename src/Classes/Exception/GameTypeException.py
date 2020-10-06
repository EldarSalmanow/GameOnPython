from src.Classes.Exception.GameException import GameException


class GameTypeException(GameException):
    def __init__(self, message):
        self.__typeError = "GameTypeException"
        self.__message = message

    def printError(self):
        print(self.__typeError + ": " + self.__message)
