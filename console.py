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
    data = file_storage.all()
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

    class FileStorage:
        __objects = {
        "BaseModel",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    }

    def all(self, cs=None):
        """ Return a dictionary of objects """
        """ Classes defined as objects """
        if cs is not None:
           if isinstance(cs, str):
            cs = self.__objects.get(cs, None)
        if cs is not None:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cs)}
        return self.__objects

    def new(self, obj):
        """Add an object to the current database session """
        """ Classes defined as object """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        self.save()



    def find_models(args):
        data = file_storage.all()
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
                objects = file_storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in file_storage.all:
                    print(file_storage.all[key])
                else:
                    print("** no instance found **")
                if args[0] not in []:
                    print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        """ Usage: Destory <class_name> <id> """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in file_storage.all():
                file_storage.all().pop(key)
                file_storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instance"""
        if not arg:
            obj_list = []
            for key, value in file_storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        elif arg in HBNBCommand.__classes:
            obj_list = []
            for key, value in file_storage.all().items():
                if arg in key:
                    obj_list.append(str(value))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return False
        elif  arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in file_storage.all():
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    obj = file_storage.all()[key]
                    setattr(obj, attr_name, attr_value)
                    obj.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """ Retrieves the number of instances of a class. """
        """ Usage: <class_name>.count()"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            count = sum(1 for key in file_storage.all() if args[0] in key)
            print(count)

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        """ And save to the JSON file """
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
