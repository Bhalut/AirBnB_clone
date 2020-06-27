#!/usr/bin/python3
"""Console Module
"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
