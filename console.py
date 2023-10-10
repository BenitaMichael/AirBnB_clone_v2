#!/usr/bin/python3
"""The command prompt class - HBNBCommand"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The command prompt class - HBNBCommand"""

    prompt = "(hbnb) "


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles Ctrl+D (EOF) to exit the program"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
