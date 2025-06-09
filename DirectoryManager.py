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
            break
        return f

    def check_directories(self):
        dir_list = self.get_directories()

        for directory in self.structure.get_structure().get("subdirectories"):
            dir_name = directory.get("name")
            dir_desc = directory.get("description")

            if dir_name in dir_list:
                print(f'[+] {dir_name}: {dir_desc}')
            else:
                print(f'[-] {dir_name}: {dir_desc}')