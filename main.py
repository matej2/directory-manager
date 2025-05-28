import cmd

from DirectoryStructure import DirectoryStructure


class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_check(self, line):
        """Checks directory structure."""
        print("Hello, World!")

    def do_str(self, line):
        structure = DirectoryStructure.get_structure()
        for d in structure["subdirectories"]:
            print(d)

    def do_q(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()