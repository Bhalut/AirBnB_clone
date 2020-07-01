#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models import storage
import json
import re


class HBNBCommand(cmd.Cmd):
    """AirBnb Clone"""
    prompt = "(hbnb) "

    def default(self, line):
        """Process commads:
            - <class name>.all()
            - <class name>.show(<id>)
            - <class name>.destroy(<id>)
            - <class name>.update(<id>, <attribute name>, <attribute value>)
            - <class name>.update(<id>, <dictionary representation>)
        Otherwise print Unknown syntax
        """
        message = "*** Unknown syntax in: {}".format(line)
        # User.show()
        if "." in line and "(" in line and ")" in line:
            args = line.split(".")
            c_name = args[0]
            c_func = args[1].split("(")[0]
            print(c_func)
            if c_func in ['all', 'show', 'count', 'update', 'destroy']:
                return

        print("*** Unknown syntax: {}".format(line))

    def do_all(self, line):
        """Prints all string representation of all instances based
           or not on the class name
        """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            l_obj = [str(value) for key, value in storage.all().items()]
            print(l_obj)
            return

        c_name = match.group(1)
        if c_name not in storage.dictionary():
            print("** class doesn't exist **")
            return

        l_obj = [str(value) for key, value in storage.all().items()
                 if (c_name == type(value).__name__)]
        print(l_obj)

    def do_create(self, line):
        """Creates a new instance, saves it (to the JSON file)
           and prints the id
        """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
            return

        c_name = match.group(1)
        if c_name not in storage.dictionary():
            print("** class doesn't exist **")
            return

        b = storage.dictionary()[line]()
        b.save()
        print(b.id)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
            return

        c_name = match.group(1)
        c_id = match.group(2)
        if c_name not in storage.dictionary():
            print("** class doesn't exist **")
            return
        if c_id is None:
            print("** instance id missing **")
            return

        key = "{}.{}".format(c_name, c_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        storage.destroy(key)

    def do_EOF(self, line):
        """Handles the End Of File"""
        return True

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
            return

        c_name = match.group(1)
        c_id = match.group(2)
        if c_name not in storage.dictionary():
            print("** class doesn't exist **")
            return
        if c_id is None:
            print("** instance id missing **")
            return

        key = "{}.{}".format(c_name, c_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** class name missing **")
            return

        c_name = match.group(1)
        c_id = match.group(2)
        c_attribute = match.group(3)
        c_value = match.group(4)
        if c_name not in storage.dictionary():
            print("** class doesn't exist **")
        elif c_id is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(c_name, c_id)
            if key not in storage.all():
                print("** no instance found **")
            elif c_attribute is None:
                print("** attribute name missing **")
            elif c_value is None:
                print("** value missing **")
            else:
                if not c_value.isdigit():
                    try:
                        c_value = float(c_value)
                    except ValueError:
                        c_value = c_value.strip('"\\')
                else:
                    c_value = int(c_value)

                setattr(storage.all()[key], c_attribute, c_value)
                storage.save()

    def emptyline(self):
        """Handles empty line"""
        return

    # Help Functions
    def help_all(self):
        """Print help all instruction"""
        msg1 = "Prints all string representation of all instances"
        msg2 = "based or not on the class name."
        msg3 = "Ex: $ all BaseModel or $ all"
        print("{} {}\n{}\n".format(msg1, msg2, msg3))

    def help_create(self):
        """Print help create instruction"""
        msg1 = "Creates a new instance, saves it(to the JSON file)"
        msg2 = "and prints the id."
        msg3 = "Ex: $ create BaseModel"
        print("{} {}\n{}\n".format(msg1, msg2, msg3))

    def help_destroy(self):
        """Print help destroy instruction"""
        msg1 = "Deletes an instance based on the class name"
        msg2 = "and id (save the change into the JSON file)."
        msg3 = "Ex: $ destroy BaseModel 1234-1234-1234"
        print("{} {}\n{}\n".format(msg1, msg2, msg3))

    def help_EOF(self):
        """Print help EOF instruction"""
        print("EOF command to exit the program\n")

    def help_show(self):
        """Print help show instruction"""
        msg1 = "Prints the string representation of an instance"
        msg2 = "based on the class name and id."
        msg3 = "Ex: $ show BaseModel 1234-1234-1234"
        print("{} {}\n{}\n".format(msg1, msg2, msg3))

    def help_quit(self):
        """Print help quit instruction"""
        print("Quit command to exit the program\n")

    def help_update(self):
        """Print help update instruction"""
        msg1 = "Updates an instance based on the class name"
        msg2 = "and id by adding or updating attribute"
        msg3 = "(save the change into the JSON file)."
        msg4 = "Ex: $ update BaseModel 1234-1234-1234 email"
        msg5 = '"aibnb@holbertonschool.com"'
        print("{} {} {}\n{} {}".format(msg1, msg2, msg3, msg4, msg5))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
