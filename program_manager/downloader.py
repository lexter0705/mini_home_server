import json
from configparser import ConfigParser

from program_manager.package.git_package import GitPackage
from git import Repo


class Downloader:
    def __init__(self, link_to_config: str):
        self.__link_to_config = link_to_config
        self.__config = {}
        self.__load_config()

    def __load_config(self):
        Repo.clone_from(self.__link_to_config, "./config")
        with open('./config/config.json', 'r') as config_file:
            self.__config = json.load(config_file)

    def download_program(self, name: str, path_to_download: str):
        package_conf = self.__config[name]
        package = GitPackage(package_conf["link_to_github"], path_to_download)
        package.download()
