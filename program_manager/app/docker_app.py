from program_manager.app.base import App
import docker
from docker.errors import NotFound

class DockerApp(App):
    def __init__(self, path: str):
        self.__path = path
        self.__docker_name = path.split("/")[-1]
        self.__client = docker.from_env()
    
    def is_worked(self) -> bool:
        return self.__client.containers.get(self.__docker_name).status == "running"

    def start(self, port: int):
        try:
            self.__client.containers.get(self.__docker_name).restart()
        except NotFound:
            image, commands = self.__client.images.build(path=self.__path)
            self.__client.containers.run(image=image, name=self.__docker_name, ports={"80/tcp": ("0.0.0.0", port)}, detach=True, remove=True)

    def stop(self):
        container = self.__client.containers.get(self.__docker_name)
        container.stop()
        container.remove()