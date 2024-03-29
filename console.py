#!/usr/bin/python3
<<<<<<< HEAD
""" Console Module """

=======
"""Defines the HBNB console."""
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
    """Contains the functionality for the HBNB console"""
=======
<<<<<<< HEAD
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignore empty spaces."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object that has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
=======
    """ Contains the functionality for the HBNB console"""
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd

    # determines prompt for interactive/non-interactive modes
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }
    dot_cmds = ["all", "count", "show", "destroy", "update"]
    types = {
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print("(hbnb)")

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ""  # initialize line elements

        # scan for general formatting - i.e '.', '(', ')'
        if not ("." in line and "(" in line and ")" in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[: pline.find(".")]

            # isolate and validate <command>
            _cmd = pline[pline.find(".") + 1: pline.find("(")]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parentheses contain arguments, parse them
            pline = pline[pline.find("(") + 1: pline.find(")")]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(", ")  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('"', "")
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if (
                        pline[0] == "{"
                        and pline[-1] == "}"
                        and type(eval(pline)) is dict
                    ):
                        _args = pline
                    else:
                        _args = pline.replace(",", "")
                        # _args = _args.replace('\"', '')
            line = " ".join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print("(hbnb) ", end="")
        return stop

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def do_create(self, args):
        """Create an object of any class"""
        if not args:
            print("** class name missing **")
            return

        # partition args (<class name>, <delim>, <params>)
        pargs = args.partition(" ")

        if pargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.classes[pargs[0]]()
        # If there are parameters.
        if pargs[2]:
            # Split the parameters.
            params = pargs[2].split(" ")

            for param in params:
                key_value = param.partition("=")
                key = key_value[0]
                value = key_value[2]

                # Skip any parameters without a value.
                # Empty strings are considered valid values.
                if not value:
                    continue

                value = value.strip()
                # Cast the value to appropriate type.
                if value[0] == '"' and value[-1] == '"':
                    value = value[1:-1].replace("_", " ").replace("\\", "")
                elif "." in value:
                    value = float(value)
                else:
                    value = int(value)

                setattr(new_instance, key, value)

        storage.new(new_instance)
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """Help information for the create method"""
        print("Creates a class of any type")
        print("[Usage]: create <className> <params>\n")

    def do_show(self, args):
        """Method to show an individual object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id and " " in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
<<<<<<< HEAD
            return

        key = c_name + "." + c_id
        try:
            print(storage.all()[key])
=======
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
        except KeyError:
            print("** no instance found **")

<<<<<<< HEAD
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
=======
    def help_show(self):
        """Help information for the show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroys a specified object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and " " in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
<<<<<<< HEAD
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if not line:
            o = storage.all()
            print([o[k].__str__() for k in o])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()
=======
            return

        key = c_name + "." + c_id

        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for the destroy command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(" ")[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(HBNBCommand.classes[args]).items():
                if k.split(".")[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """Help information for the all command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage.all(HBNBCommand.classes[args]).items():
            if args == k.split(".")[0]:
                count += 1
        print(count)
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e

            o = storage.all(eval(args[0]))
            print([o[k].__str__() for k in o])

<<<<<<< HEAD
        except NameError:
            print("** class doesn't exist **")
=======
    def do_update(self, args):
<<<<<<< HEAD
        """Updates a certain object with new info"""
        c_name = c_id = att_name = att_val = kwargs = ""

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
=======
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
<<<<<<< HEAD
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """count the number of instances of a class
        """
        counter = 0
        try:
            my_list = split(line, " ")
            if my_list[0] not in self.__classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == my_list[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
=======
            return

        # first determine if kwargs or args
        if "{" in args[2] and "}" in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '"':  # check for quoted arg
                second_quote = args.find('"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(" ")

            # if att_name was not quoted arg
            if not att_name and args[0] != " ":
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '"':
                att_val = args[2][1: args[2].find('"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(" ")[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if i % 2 == 0:
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """Help information for the update class"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e
