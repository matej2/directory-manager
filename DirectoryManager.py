import os
from typing import LiteralString

from DirectoryStructure import DirectoryStructure


class DirectoryManager:
    def __init__(self, structure: DirectoryStructure):
        self.structure = structure
        self.path = os.getcwd()

    def get_directories(self):
        f = []
        for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
            f.extend(filenames)
            break
        return f

    def check_directories(self):
        structure = self.structure.get_structure().get("subdirectories")

        print(f"Directory structure analysis for {self.path}:")

        self.check_subdirectories(structure, 0)

    def create_directories(self):
        structure = self.structure.get_structure().get("subdirectories")

        self.create_subdirectories(structure, os.getcwd())

    def get_subdirectory_path(self, dir):
        os.path.relpath(dir, self.path)

    def create_subdirectories(self, dir_structure: dict, current_dir: LiteralString | str | bytes):
        for directory in dir_structure:
            dir_name = directory.get("name")
            dir_subdir = directory.get("subdirectories")
            dir_type = directory.get("type")

            if dir_type == "directory":
                current_dir = os.path.join(str(current_dir), dir_name)
                os.mkdir(current_dir)


            if len(dir_subdir) > 0:
                self.create_subdirectories(dir_subdir, current_dir)


    def check_subdirectories(self, dir_structure: dict, level: int):
        for directory in dir_structure:
            dir_name = directory.get("name")
            dir_desc = directory.get("description")
            dir_subdir = directory.get("subdirectories")
            dir_level = ""

            i = 0
            while i < level:
                dir_level += "│   "
                i += 1

            if self.structure.does_exist(dir_name) is not None:
                print(f'[+] {dir_level}├── {dir_name}:'.ljust(40) + dir_desc)
            else:
                print(f'[-] {dir_level}├── {dir_name}:'.ljust(40) + dir_desc)

            if len(dir_subdir) > 0:
                self.check_subdirectories(dir_subdir, (level+1))

