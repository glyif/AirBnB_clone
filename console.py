#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - class for HBNB cli
    
    inherits from cmd.Cmd
    """
    prompt = "(hbnb) "

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
        functions = {
                "BaseModel" : BaseModel,
                "Amenity"   : Amenity,
                "City"      : Place,
                "Review"    : Review,
                "State"     : State
                }
        if arg not in functions.keys():
            print("** class doesn't exist **")
        else:
            model = functions[arg]()
            model.save()
            print("{}".format(model.id))

    def do_show(self, arg):
        args = arg.split()
        if len(args) != 2:
            print("** class name missing **")
            return

        if (self.validate_instance(args[0], args[1])):
            instance = storage.all()
            print(instance[args[1]])
        else:
            return

    def do_destroy(self, arg):
        args = arg.split()
        instance = storage.all()
        del(instance[args[1]])
        storage.save()

    def do_update(self, arg):
        args = arg.split()
        instance = storage.all()
        setattr(instance[args[1]], args[2], args[3])
        storage.save()
    
    def do_all(self, arg):
        args = arg.split()
        instance_list = []
        instance = storage.all()

        if len(args) < 1:
            for value, count in instance.items():
                instance_list.append(str(instance[value]))
            print("{}".format(instance_list))
        else:
            for value, count in instance.items():
                if instance[value].__class__.__name__ == args[0]:
                    instance_list.append(str(instance[value]))
            print("{}".format(instance_list))

    """ prevent empty line + ENTER from exectuing lastcmd"""
    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    @staticmethod
    def validate_input(arg):
        class_list = ["BaseModel"]
        if arg[0] not in class_list:
            print("** class doesn't exist **")
            return
        return (arg[0])

    @staticmethod
    def validate_len(arg, length, message):
        if len(arg) < length:
            print(message)
            return (None)
        else:
            return (arg)

    @staticmethod
    def validate_instance(class_name, id):
        master_json = storage.all()
        if id in master_json.keys():
            if master_json[id].__class__.__name__ == class_name:
                return (id)
        print("** instance id missing **")
        return (None)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
