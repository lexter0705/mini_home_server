import abc


class App(abc.ABC):
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
    @abc.abstractmethod
    def port(self) -> str:
        pass