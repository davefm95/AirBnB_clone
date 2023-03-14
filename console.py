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
            clsmod = {'BaseModel': "models.base_model",
                      'User': "models.user",
                      'Place': "models.place",
                      'State': "models.state",
                      'City': "models.city",
                      'Amenity': "models.amenity",
                      'Review': "models.review"
                     }
            for k, v in clsmod.items():
                if k == arg:
                    mymod = import_module(v)
                    mycls = getattr(mymod, arg)
                    obj = mycls()
                    obj.save()
                    print(obj.id)
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

    def do_destroy(self, arg):
        """deletes an instance from the file"""
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
                    del objs[key]
                    storage.save()
                    return
        if isvalidclass == 1:
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string rep of objs"""
        objs = storage.all()
        if not arg:
            for v in objs.values():
                print(v)
            return
        isvalidclass = 0
        for k in objs.keys():
            if arg == k.split(".")[0]:
                isvalidclass = 1
                print(objs[k])
        if not isvalidclass:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """updates an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        objs = storage.all()
        lst = []
        for key in objs.keys():
            lst.append(key.split(".")[0])
            lst.append(key.split(".")[1])
        if args[0] not in lst:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("**instance id missing **")
            return
        if args[1] not in lst:
            print("**no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj_id = args[0] + "." + args[1]
        obj = objs[obj_id]
        if args[3][0] == '"':
            string = args[3]
            for i in range(4, len(args)):
                string = string + " " + args[i]
                if args[i][-1] == '"':
                    args[3] = string
                    break
            args[3] = args[3][1:-1]
        elif "." in args[3]:
            try:
                float(args[3])
            except ValueError:
                pass
        else:
            try:
                int(args[3])
            except ValueError:
                pass
        obj.__dict__[args[2]] = args[3]
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
