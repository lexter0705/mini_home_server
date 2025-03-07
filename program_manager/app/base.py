import abc


class App(abc.ABC):
    def __init__(self, port: str):
        self.__port = port

    @abc.abstractmethod
    def is_worked(self):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @property
    def port(self) -> str:
        return self.__port
