#!/usr/bin/python3
"""The console.py Script"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """The Hbnb class """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """overwrites default behaviour for empty line"""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
