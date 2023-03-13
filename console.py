#!/usr/bin/python3
"""The console.py Script"""
import cmd
from importlib import import_module
from models import storage


class HBNBCommand(cmd.Cmd):
    """The Hbnb class """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """overwrites default behaviour for empty line"""
        pass

    def do_EOF(self, arg):
        """Handles eof character"""
        print()
        return True

    def do_create(self, arg):
        """Creates an instance"""
        if not arg:
            print("** class name missing **")
            return
        else:
            clsmod = {'BaseModel': "models.base_model"}
            for k, v in clsmod.items():
                if k == arg:
                    mymod = import_module(v)
                    mycls = getattr(mymod, arg)
                    obj = mycls()
                    obj.save()
                    print(f"{obj.id}")
                    return
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints string rep of an instance"""
        args = arg.split()
        objs = storage.all()
        if not args:
            print("** class name missing **")
            return
        isvalidclass = 0
        for key in objs.keys():
            if args[0] == key.split(".")[0]:
                isvalidclass = 1
                if len(args) == 1:
                    print("** instance id missing**")
                    return
                if args[1] == key.split(".")[1]:
                    print(objs[key])
                    return
        if isvalidclass == 1:
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
