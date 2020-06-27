#!/usr/bin/python3
"""Console Module
"""
import cmd
import sys
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id """
        if line in [None, ""]:
            print("** class name missing **")
        elif storage.classes(line):
            print("** class doesn't exist **")
        else:
            b = storage.create()[line]()
            b.save()
            print(b.id)

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
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
