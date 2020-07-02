#!/usr/bin/python3
""" test_console.py

    Test of console.py file
"""
import unittest
import console
import pep8
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class testConsole(unittest.TestCase):
    """TestConsole Class

    Test cases of console.py
    """

    def test_pep8_console(self):
        """test_pep8_console test

        Test pep8 for console.py file
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_console_prompt(self):
        """test if prompt is correct

        Functionality test
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


    def test_docstrings(self):
        """test if docstrings exist alredy"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", out.getvalue().strip())
