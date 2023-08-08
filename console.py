#!/usr/bin/env python3
"""Contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This module contains the entry point to the command interpreter"""
    def __init__(self):
        """Initializes the class"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the console"""
        return True

    def do_quit(self, line):
        """Quits the console"""
        return True

    def emptyline(self):
        """states what happens when a line is empty"""
        pass

    def postloop(self):
        """gives a new line after exicting the console"""
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
