import os
from os import listdir

from DirectoryStructure import DirectoryStructure


class DirectoryManager:
    def __init__(self, structure: DirectoryStructure):
        self.structure = structure

    def get_directories(self):
        f = []
        for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
            f.extend(filenames)
        return f

    def check_directories(self):
        dir_list = self.get_directories()
        structure = self.structure.get_structure().get("subdirectories")

        self.check_subdirectories(dir_list, structure)

    def check_subdirectories(self, dir_list: list[str], dir_structure: dict):
        for directory in dir_structure:
            dir_name = directory.get("name")
            dir_desc = directory.get("description")
            dir_subdir = directory.get("subdirectories")

            if dir_name in dir_list:
                print(f'[+] {dir_name}: {dir_desc}')
            else:
                print(f'[-] {dir_name}: {dir_desc}')

            if len(dir_subdir) > 0:
                self.check_subdirectories(dir_list, dir_subdir)
