from program_manager.app.base import App


class DockerApp(App):
    def __init__(self, path: str, port: str):
        self.__path = path
        self.__port = port
        self.__docker_id = ""
    
    def is_worked(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass
    
    @property
    def port(self) -> str:
        return self.__port