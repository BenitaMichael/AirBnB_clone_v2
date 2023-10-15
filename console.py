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

class HBNBCommand(cmd.Cmd):
    """The command prompt class - HBNBCommand"""

    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        self.classes = {
            "BaseModel"
            "Place"
            "State"
            "City"
            "Amenity"
            "Review"
            "User"
        }

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


    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = file_storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        """ Usage: Destory <class_name> <id> """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = file_storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                del objects[key]
                file_storage.save()
            else:
                print("** no instance found **")


    def do_all(self, arg):
        """Print string representation of all instance"""
        """Print all instances or all instances of a specific class"""
        args = arg.split()
        if not arg:
            print([str(obj) for obj in file_storage.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = file_storage.all()[class_name]
            if instances:
                print([str(obj) for obj in instances.values()])
            else:
                print("No instances found for class: {}".format(class_name))

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return False
        elif  arg_list[0] not in self.classes:
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
        """Usage: count <className> or <className>.count()
        retrieves the number of instances of a class
        """
        """Count the number of instances for a specific class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = file_storage.all(class_name)
            count = len(instances)
            print(count)

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        """ And save to the JSON file """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

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
