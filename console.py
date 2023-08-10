#!/usr/bin/env python3
"""Contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This module contains the entry point to the command interpreter"""
    prompt = "(hbnb) "
    MODELS = ['BaseModel', 'User', 'Place', 'State', 'City',
              'Amenity', 'Review']

    def do_EOF(self, line):
        """Exits the console"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """states what happens when a line is empty"""
        pass

    def postloop(self):
        """gives a new line after exicting the console"""
        print()

    def do_create(self, line):
        """TO create an instance of the base model"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            command = args[0]
            if command not in self.MODELS:
                print("** class doesn't exist **")
            else:
                new_instance = self.MODELS[command]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """Prints the string instance based on the class name"""

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

    def do_all(self, line):
        """Prints all instances based or not on the class name"""

    def do_update(self, line):
        """ Updates an instance based on the class name and id"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()
