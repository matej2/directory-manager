import cmd

from DirectoryManager import DirectoryManager
from DirectoryStructure import DirectoryStructure


class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to DirectoryManager. Type "help" for available commands.'

    def __init__(self):
        super().__init__()
        self.structure = DirectoryStructure()
        self.manager = DirectoryManager(self.structure)

    def do_check(self, line):
        """Checks directory structure."""
        self.manager.check_directories()

    def do_q(self):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()