import abc


class Package(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def download(self):
        pass
    
    @abc.abstractmethod
    def delete(self):
        pass