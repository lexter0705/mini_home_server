import json
from git import Repo
import os

class ConfigParser:
    def __init__(self, link_to_config: str):
        self.__config = {}
        self.__parse(link_to_config)

    def __parse(self, link_to_config: str):
        if os.path.exists(link_to_config):
            Repo.clone_from(link_to_config, "./config")
        with open('./config/config.json', 'r') as config_file:
            self.__config = json.load(config_file)

    @property
    def config(self):
        return self.__config
