#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
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
        class_list = ["BaseModel"]
        if arg not in class_list:
            print("** class doesn't exist **")
        if (arg == "BaseModel"):
            model = BaseModel()
            model.save()
            print("{}".format(model.id))

    def do_show(self, arg):
        args = arg.split()
        instance = storage.all()
        print(instance[args[1]])

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
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
