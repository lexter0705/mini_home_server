import abc


class App(abc.ABC):
    @abc.abstractmethod
    def is_worked(self):
        pass

    @abc.abstractmethod
    def start(self, port: int):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
