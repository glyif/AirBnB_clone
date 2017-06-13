#!/usr/bin/python3
import cmd
import inspect
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - class for HBNB cli

    inherits from cmd.Cmd
    """
    prompt = "(hbnb) "

    functions = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
        }

    def do_quit(self, arg):
        """
        quit - quits from the cli

        Args:
        @self: self
        @arg: argument
        """
        return True

    def do_EOF(self, arg):
        """
        EOF - end of file

        Args:
        @self: self
        @arg: argument
        """
        return True

    def do_create(self, arg):
        """
        do_create - creates a class

        Args:
        @self: self
        @arg: argument
        """
        args = arg.split()
        if self.input_validation(args):
            model = self.functions[arg]()
            model.save()
            print("{}".format(model.id))

    def do_show(self, arg):
        """
        do_show - prints the __str__ of a specific obj

        Args:
        @self: self
        @arg: argument
        """
        args = arg.split()
        if self.input_validation(args):
            instance = storage.all()
            for key, value in instance.items():
                instance_id = key.split('.')[1]
                if instance_id == args[1]:
                    print(instance.get(key))
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        do_destroy - delete/destroys an object

        Args:
        @self: self
        @arg: argument
        """
        args = arg.split()
        if self.input_validation(args):
            instance = storage.all()
            for key in list(instance):
                instance_id = key.split('.')[1]
                if instance_id == args[1]:
                    instance.pop(key, 0)
                    storage.save()

    def do_update(self, arg):
        """
        do_update - updates an object

        Args:
        @self: self
        @arg: argument
        """
        args = arg.split()
        if self.update_validate(args):
            instance = storage.all()
            for key, value in instance.items():
                instance_id = key.split('.')[1]
                if instance_id == args[1]:
                    value = self.type_checker(args[3])
                    setattr(instance.get(key), args[2], value)
                    storage.save()

    def do_all(self, arg):
        """
        do_all - prints all

        Args:
        @self: self
        @arg: arguments
        """
        args = arg.split()
        instance_list = []
        instance = storage.all()

        if len(args) < 1:
            for value, count in instance.items():
                instance_list.append(str(instance[value]))
            print("{}".format(instance_list))
        else:
            if args[0] not in self.functions.keys():
                print("** class doesn't exist **")
                return
            for value, count in instance.items():
                if instance[value].__class__.__name__ == args[0]:
                    instance_list.append(str(instance[value]))
            print("{}".format(instance_list))

    def do_User(self, arg):
        if arg == ".all()":
            self.do_all("User")

    """ prevent empty line + ENTER from exectuing lastcmd"""
    def emptyline(self):
        return False

    @staticmethod
    def input_validation(args):
        """
        input_validation - validates input router

        static method
        @args: list arguments
        """
        function = inspect.stack()[1][3]
        if function == "do_create":
            return (HBNBCommand.class_validate(args))
        elif function == "do_show":
            return (HBNBCommand.instance_validate(args))
        elif function == "do_destroy":
            return (HBNBCommand.instance_validate(args))
        elif function == "do_update":
            return (HBNBCommand.update_validate(args))

    @staticmethod
    def class_validate(args):
        """
        class_validate - validates a class arg

        static method
        Args:
        @args: list of arguments
        """
        if len(args) < 1:
            print("** class name missing **")
            return (False)
        if args[0] not in list(HBNBCommand.functions):
            print("** class doesn't exist **")
            return (False)
        return (True)

    @staticmethod
    def instance_validate(args):
        """
        instance_validate - validates instance

        staticmethod
        Args:
        @args: list of arguments
        """
        if len(args) < 2:
            print("** instance id missing **")
            return (False)
        return(HBNBCommand.class_validate(args))

    @staticmethod
    def update_validate(args):
        """
        update_validate - validate update arguments

        Args:
        @args: arguments
        """
        if HBNBCommand.instance_validate(args):
            if len(args) < 3:
                print("** attribute name missing **")
                return (False)
            elif len(args) < 4:
                print("** value missing **")
                return (False)
            return (True)
        return (False)

    @staticmethod
    def type_checker(arg):
        check_list = list(arg)
        if check_list[0] == "'" or check_list[0] == '"':
            new_string = ''.join([c for c in arg if c != '"' and c != "'"])
            return (new_string)
        if ord(check_list[0]) >= 48 and ord(check_list[0]) <= 57:
            return (int(arg))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
