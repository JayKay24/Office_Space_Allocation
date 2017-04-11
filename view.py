"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    view.py create_room <room_type> <room_name>
    view.py add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    view.py (-i | --interactive)
    view.py (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from controller import create_office
from controller import create_living_space

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class MyInteractive (cmd.Cmd):
    prompt = '(view) '
    file = None
    @docopt_cmd
    def create_new_room(self, args):
        """Usage: create_room <room_type> <room_name>"""
        if args["<room_type>"] == "Office":
            print(create_office(args))
        elif args["<room_type>"] == "LivingSpace":
            print(create_living_space(args))

    @docopt_cmd
    def add_new_person(self, args):
        """Usage: add_person <person_name> <FELLOW|STAFF> [wants_accomodation]"""
        print(add_person(args))
        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:

    MyInteractive().cmdloop()
