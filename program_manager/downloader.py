from program_manager.config_parser import ConfigParser
from program_manager.package.git_package import GitPackage


class Downloader:
    def __init__(self, config: ConfigParser):
        self.__config = config

    def download_program(self, name: str, path_to_download: str):
        package_conf = self.__config.config[name]
        package = GitPackage(package_conf["repo"],
            f"{path_to_download}/{name}")
        package.download()
