from program_manager.app.base import App
from program_manager.package.base import Package


class Program:
    def __init__(self, package: Package, app: App):
        self.__package = package
        self.__app = app

    def update(self):
        self.__app.stop()
        self.__package.update()
        self.__app.start()

    def delete(self):
        self.__app.stop()
        self.__package.delete()

    def stop(self):
        self.__app.stop()

    def start(self):
        self.__app.start()