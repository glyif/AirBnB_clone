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
        arg = arg.split()
        if (not self.validate_len(arg, 1, "** class name missing **")):
                return
        v_input = self.validate_input(arg)
        if (v_input == "BaseModel"):
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

    def validate_input(self, arg):
        class_list = ["BaseModel"]
        if arg[0] not in class_list:
            print("** class doesn't exist **")
            return
        return (arg[0])

    def validate_len(self, arg, length, message):
        if len(arg) < length:
            print(message)
            return (None)
        else:
            return (arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
