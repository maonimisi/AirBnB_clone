#!/usr/bin/env python3
"""Contains the entry point of the command interpreter"""

import cmd
import json
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This module contains the entry point to the command interpreter"""
    prompt = "(hbnb) "
    MODELS = {
        "City": City,
        "User": User,
        "Place": Place,
        "State": State,
        "Review": Review,
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        }

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


"""
    def do_create(self, line):
        """TO create an instance of the base model"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            command = args[0]
            model = self.MODELS.get(command)
            if model:
                new_instance = model()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
"""

    def do_create(self, line):
        """TO create an instance of the base model"""
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            command = args[0]
            if not command:
                print("** class name missing **")  # Here
            else:
                model = self.MODELS.get(command)
                if model:
                    new_instance = model()
                    new_instance.save()
                    print(new_instance.id)
                else:
                    print("** class doesn't exist **")

"""
    def do_show(self, line):
        """Prints the string instance based on the class name"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        command = args[0]
        if command not in self.MODELS:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = (f"{command}.{instance_id}")
        all_objects = storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")
"""

    def do_show(self, line):
        """Prints the string instance based on the class name"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        command = args[0]
        if command not in self.MODELS:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = (f"{command}.{instance_id}")
        all_objects = storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

"""
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        command = args[0]
        if command not in self.MODELS:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{command}.{instance_id}"
        all_objects = storage.all()
        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")
"""

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        command = args[0]
        if command not in self.MODELS:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{command}.{instance_id}"
        all_objects = storage.all()
        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")
    
    """
    def do_all(self, line):
        """Prints all instances based or not on the class name"""
        args = line.split()
        if not args:
            all_objects = storage.all()
            for key, instance_id in all_objects.items():
                if instance_id.__class__.__name__ == command:
                    print(instance_id)
        else:
            command = args[0]
            if command not in self.MODELS:
                print("** class doesn't exist **")
                return
            all_objects = storage.all()
            for key, instance_id in all_objects.items():
                if instance_id.__class__.__name__ == command:
                    print(instance_id)
"""

    def do_all(self, line):
        """Prints all instances based or not on the class name"""
        args = line.split()
        if not args:
            all_objects = storage.all()
            instance_list = []
            for key, instance_id in all_objects.items():
                if instance_id.__class__.__name__ == command:
                    instance_list.append(str(instance_id))
            print(instance_list)  # Here
        else:
            command = args[0]
            if command not in self.MODELS:
                print("** class doesn't exist **")
                return
            all_objects = storage.all()
            instance_list = []
            for key, instance_id in all_objects.items():
                if instance_id.__class__.__name__ == command:
                    instance_list.append(str(instance_id))
            print(instance_list)

"""
    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        command = args[0]
        if command not in self.MODELS:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{command}.{instance_id}"
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = all_objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()
"""
     def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        command = args[0]
        if command not in self.MODELS:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{command}.{instance_id}"
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** attribute cannot be updated **")
            return

        attribute_value = args[3]

        instance = all_objects[key]
        if hasattr(instance, attribute_name):
            attr_type = type(getattr(instance, attribute_name))
            try:
                casted_value = attr_type(attribute_value)
            except ValueError:
                print("** invalid value type **")
                return
            setattr(instance, attribute_name, casted_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == "__main__":
    if sys.stdin.isatty() and sys.stdout.isatty():
        HBNBCommand().cmdloop()
    else:
        with sys.stdin as input_file:
            HBNBCommand(stdin=input_file).cmdloop()
