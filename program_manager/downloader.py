from program_manager.package.git_package import GitPackage
from program_manager.app.docker_app import DockerApp
from program_manager.program import Program


class Downloader:
    def __init__(self, link_to_config: str, path_to_download: str):
        self.__link_to_config = link_to_config
        self.__path_to_download = path_to_download
        self.__config = {}
        self.__load_config()

    def __load_config(self):
        pass

    def download_program(self, name: str) -> Program:
        package_conf = self.__config[name]
        package = GitPackage(package_conf["link_to_github"], self.__path_to_download)
        package.download()
        app = DockerApp(f"{self.__path_to_download}/{package_conf["link_to_github"].split("/")[-1]}",
                        package_conf["port"])
        return Program(package, app)
