from program_manager.program import Program


class Programs:
    def __init__(self, downloader):
        self.__programs: dict[int, Program] = {}

    def __getitem__(self, item: int):
        return self.__programs[item]

    def __len__(self):
        return len(self.__programs)

    def add_program(self, program: Program):
        pass
