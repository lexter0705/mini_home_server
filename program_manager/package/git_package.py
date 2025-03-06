from program_manager.package.base import Package


class GitPackage(Package):
    def __init__(self, link_to_repos: str, path_to_download: str):
        self.__link_to_repos = link_to_repos
        self.__path_to_download = path_to_download

    def update(self):
        pass

    def download(self):
        pass
    
    def delete(self):
        pass