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
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                try:
                    instance = BaseModel().get(class_name, instance_id)
                    if instance:
                        print(instance)
                    else:
                        print("** no instance found **")
                except NameError:
                    print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                try:
                    instance = BaseModel().get(class_name, instance_id)
                    if instance:
                        instance.delete()
                    else:
                        print("**  no instance found **")
                except NameError:
                     print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representation of all instance"""
        args = arg.split()
        if not args:
            print([str(inst) for inst in BaseModel().all()])
        else:
            class_name = args[0]
            try:
                print([str(inst) for inst in BaseModel().all(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                if len(args) < 3:
                    print("** attribute name missing **")
                else:
                    if len(args) < 4:
                        print("** value missing **")
                    else:
                         try:
                            instance = BaseModel().get(class_name, instance_id)
                            if instance:
                                attribute_name = args[2]
                                attribute_value = args[3]
                                try:
                                    attribute_value = eval(attribute_value)
                                except (NameError, SyntaxError):
                                    pass
                                setattr(instance, attribute_name, attribute_value)
                                instance.save()
                            else:
                                print("** no  instance found **")
                         except NameError:
                            print("** class doesn't exist **")

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
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
