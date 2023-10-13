#!/usr/bin/python3
"""The command prompt class - HBNBCommand"""

import cmd
import sys
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

def find_models(args):
    data = storage.all()
    data_list = []
    arg_list = split_arg(args)
    classes = {
        "BaseModel",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    }


class HBNBCommand(cmd.Cmd):
    """The command prompt class - HBNBCommand"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    }


    def find_models(args):
        data = storage.all()
        data_list = []
        arg_list = split_arg(args)
        __classes = {
        "BaseModel",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    }
  

    def do_show(self, arg):
        """Print the string representation of an sample"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if len(args) < 2:
                print("** sample id missing **")
            else:
                sample_id = args[1]
                try:
                    sample = BaseModel().get(class_name, sample_id)
                    if sample:
                        print(sample)
                    else:
                        print("** sample not found **")
                except NameError:
                    print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        """Delete an sample based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if len(args) < 2:
                print("** sample id missing **")
            else:
                sample_id = args[1]
                try:
                    sample = BaseModel().get(class_name, sample_id)
                    if sample:
                        sample.delete()
                    else:
                        print("** sample not found **")
                except NameError:
                     print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representation of all sample"""
        args = arg.split()
        if not args:
            print([str(samp) for samp in BaseModel().all()])
        else:
            class_name = args[0]
            try:
                print([str(samp) for samp in BaseModel().all(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an samp based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if len(args) < 2:
                print("** sample id missing **")
            else:
                sample_id = args[1]
                if len(args) < 3:
                    print("** attribute name missing **")
                else:
                    if len(args) < 4:
                        print("** value missing **")
                    else:
                         try:
                            sample = BaseModel().get(class_name, sample_id)
                            if sample:
                                attribute_name = args[2]
                                attribute_value = args[3]
                                try:
                                    attribute_value = eval(attribute_value)
                                except (NameError, SyntaxError):
                                    pass
                                setattr(sample, attribute_name, attribute_value)
                                sample.save()
                            else:
                                print("** sample not found **")
                         except NameError:
                            print("** class doesn't exist **")

    def do_create(self, arg):
        """Create a new sample of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_sample = eval(arg)()
                new_sample.save()
                print(new_sample.id)
            except NameError:
                print("** class doesn't exist **")  

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles Ctrl+D (EOF) to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
