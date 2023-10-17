#!/usr/bin/python3
"""The command prompt class - HBNBCommand"""

import cmd
import json
from models import dataStorage
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {
            "BaseModel"
            "Place"
            "State"
            "City"
            "Amenity"
            "Review"
            "User"
            }

class HBNBCommand(cmd.Cmd):
    """The command prompt class - HBNBCommand"""

    prompt = "(hbnb) "

    classes = {
        "BaseModel"
        "Place"
        "State"
        "City"
        "Amenity"
        "Review"
        "User"
        }

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


    def do_update(self, arg):
        """Update an instance based on class name and id with a new attribute value"""
        args = arg.split()
        objects = dataStorage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                obj = objects[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances or based on class name"""
        args = arg.split()
        objects = dataStorage.all()
        if not args:
            print([str(objects[obj]) for obj in objects])
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            filtered_objects = {obj: objects[obj] for obj in objects if obj.startswith(args[0] + ".")}
            print([str(filtered_objects[obj]) for obj in filtered_objects])


    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = dataStorage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                del objects[key]
                dataStorage.save()
            else:
                print("** no instance found **")

    def do_show(self, arg):
        """Print the string representation of an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = dataStorage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
