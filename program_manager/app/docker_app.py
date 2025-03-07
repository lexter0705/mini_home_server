from program_manager.app.base import App
import docker


class DockerApp(App):
    def __init__(self, path: str, port: str):
        super().__init__(port)
        self.__path = path
        self.__docker_name = path.split("/")[-1]
        self.__client = docker.from_env()
    
    def is_worked(self) -> bool:
        pass

    def start(self):
        image, commands = self.__client.images.build(path=self.__path, dockerfile='Dockerfile')
        self.__client.containers.run(image=image, ports={"80/tcp": ("0.0.0.0", int(self.port))}, name=self.__docker_name)

    def stop(self):
        pass