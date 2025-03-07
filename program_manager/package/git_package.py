import os

from git import Repo

from program_manager.package.base import Package


class GitPackage(Package):
    def __init__(self, link_to_repos: str, path_to_download: str):
        self.__link_to_repos = link_to_repos
        self.__path_to_download = path_to_download
        self.__repo: Repo | None = Repo(path_to_download) if os.path.isdir(path_to_download) else None

    def update(self):
        if self.__repo is None:
            raise Exception('Repo not downloaded')

        self.__repo.remotes.origin.pull()

    def delete(self):
        if self.__repo is None:
            raise Exception('Repo not downloaded')

        os.remove(f"{self.__path_to_download}")

    def download(self):
        self.__repo = Repo.clone_from(self.__link_to_repos, self.__path_to_download)
