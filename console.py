#!/usr/bin/python3
import cmd

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
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
