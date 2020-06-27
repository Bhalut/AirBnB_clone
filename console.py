#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """AirBnb Clone"""
    prompt = "(hbnb) "

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name
        """
        if line != "":
            args = line.split(" ")
            if storage.classes(args[0]):
                print("** class doesn't exist **")
            else:
                l_obj = [str(value) for key, value in storage.all().items()
                         if (type(value).__name__ == args[0])]
                print(l_obj)
        else:
            l_obj = [str(value) for key, value in storage.all().items()]
            print(l_obj)

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)\
            and prints the id
        """
        if line in [None, ""]:
            print("** class name missing **")
        elif storage.classes(line):
            print("** class doesn't exist **")
        else:
            b = storage.create()[line]()
            b.save()
            print(b.id)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = line.split(" ")
        if line in [None, ""]:
            print("** class name missing **")
        elif storage.classes(args[0]):
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                key = "{}.{}".format(args[0], args[1])

            if key in storage.all():
                storage.destroy(key)
            else:
                print("** no instance found **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split(" ")
        if line in [None, ""]:
            print("** class name missing **")
        elif storage.classes(args[0]):
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                key = "{}.{}".format(args[0], args[1])

            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_EOF(self, line):
        """Handles the End Of File"""
        return True

    def do_quit(self, line):
        """Exit programm"""
        return True

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""
        args = line.split(" ")
        # className = args[0]
        # iD = args[1]
        # attribute = args[2]
        # attributeValue = args[3]
        if line in [None, ""]:
            print("** class name missing **")
        elif storage.classes(args[0]):
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                key = "{}.{}".format(args[0], args[1])

            if key in storage.all():
                for k, v in storage.all().items():
                    if k == args[2]:
                        if args in [None, ""]:
                            print("** value missing **")
                        else:
                            storage.all()[k] = args[3]
                    else:
                        print("** attribute name missing **")
            else:
                print("** no instance found **")

    def emptyline(self):
        """Handles empty line"""
        return

    def help_quit(self):
        """Print quit instruction"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
