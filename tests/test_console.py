#!/usr/bin/python3
""" Test file all unittests for console and all features"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None
        try:
            os.remove("file.json")
        except:
            pass

    def capture_stdout(self, command):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(command)
            return f.getvalue()

    def test_quit(self):
        output = self.capture_stdout("quit")
        self.assertEqual(output, "")
        self.assertTrue(self.console.quit)

    def test_EOF(self):
        output = self.capture_stdout("EOF")
        self.assertEqual(output, "")
        self.assertTrue(self.console.quit)

    def test_create(self):
        output = self.capture_stdout("create BaseModel")
        self.assertTrue(len(output) > 0)
        self.assertIn("created_at", output)
        self.assertIn("id", output)

    def test_create_missing_class(self):
        output = self.capture_stdout("create")
        self.assertIn("** class name missing **", output)

    def test_create_nonexistent_class(self):
        output = self.capture_stdout("create MyModel")
        self.assertIn("** class doesn't exist **", output)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            output = self.capture_stdout(f"show BaseModel {obj_id}")
            self.assertIn("created_at", output)
            self.assertIn("id", output)

    def test_show_missing_class(self):
        output = self.capture_stdout("show")
        self.assertIn("** class name missing **", output)

    def test_show_nonexistent_class(self):
        output = self.capture_stdout("show MyModel")
        self.assertIn("** class doesn't exist **", output)

    def test_show_missing_id(self):
        output = self.capture_stdout("show BaseModel")
        self.assertIn("** instance id missing **", output)

    def test_show_nonexistent_instance(self):
        output = self.capture_stdout("show BaseModel 1234-1234-1234")
        self.assertIn("** no instance found **", output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        output = self.capture_stdout(f"destroy BaseModel {obj_id}")
        self.assertTrue(len(output) == 0)

    def test_destroy_missing_class(self):
        output = self.capture_stdout("destroy")
        self.assertIn("** class name missing **", output)

    def test_destroy_nonexistent_class(self):
        output = self.capture_stdout("destroy MyModel")
        self.assertIn("** class doesn't exist **", output)

    def test_destroy_missing_id(self):
        output = self.capture_stdout("destroy BaseModel")
        self.assertIn("** instance id missing **", output)

    def test_destroy_nonexistent_instance(self):
        output = self.capture_stdout("destroy BaseModel 1234-1234-1234")
        self.assertIn("** no instance found **", output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
        output = self.capture_stdout("all BaseModel")
        self.assertTrue(len(output) > 0)
        self.assertIn("BaseModel", output)

    def test_all_empty_class(self):
        output = self.capture_stdout("all")
        self.assertTrue(len(output) > 0)

    def test_all_nonexistent_class(self):
        output = self.capture_stdout("all MyModel")
        self.assertIn("** class doesn't exist **", output)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        output = self.capture_stdout(f"update BaseModel {obj_id} first_name 'John'")
        self.assertTrue(len(output) == 0)

    def test_update_missing_class(self):
        output = self.capture_stdout("update")
        self.assertIn("** class name missing **", output)

    def test_update_nonexistent_class(self):
        output = self.capture_stdout("update MyModel")
        self.assertIn("** class doesn't exist **", output)

    def test_update_missing_id(self):
        output = self.capture_stdout("update BaseModel")
        self.assertIn("** instance id missing **", output)

    def test_update_nonexistent_instance(self):
        output = self.capture_stdout("update BaseModel 1234-1234-1234")
        self.assertIn("** no instance found **", output)

    def test_update_missing_attribute_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        output = self.capture_stdout(f"update BaseModel {obj_id}")
        self.assertIn("** attribute name missing **", output)

    def test_update_missing_attribute_value(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        output = self.capture_stdout(f"update BaseModel {obj_id} first_name")
        self.assertIn("** value missing **", output)

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
        output = self.capture_stdout("User.count()")
        self.assertEqual(output, "1\n")

if __name__ == '__main__':
    unittest.main()

