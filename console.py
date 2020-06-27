#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
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

    def emptyline(self):
        """Handles empty line"""
        return

    def do_EOF(self, line):
        """Handles the End Of File"""
        return True

    def do_quit(self, line):
        """Exit programm"""
        return True

    def help_quit(self):
        """Print quit instruction"""
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
