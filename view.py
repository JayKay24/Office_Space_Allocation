"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    view create_room <room_type> <room_name>...
    view add_person <fname> <lname> <person_job> [<want_accommodation>]
    view display_all_offices
    view print_room <room_name>
    view display_full_offices
    view display_employee_office <fname> <lname>
    view (-i | --interactive)
    view (-h | --help)
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
from controller import create_person
from controller import display_persons_office
from controller import display_offices
from controller import display_room
from model import offices, fellows, staffs, full_offices, full_living_spaces

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
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = args['<room_type>']
        room_name = args['<room_name>']

        for item in room_name:
        	if room_type.upper() == "OFFICE":
        		create_office(item)
        	elif room_type.upper() == "LIVING":
        		create_living_space(item)


    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <fname> <lname> <person_job> [<want_accommodation>]"""
        job_status = args['<person_job>']
        person_fname = args['<fname>']
        person_lname = args['<lname>']
        accom = args['<want_accommodation>']
        person = create_person(person_fname, person_lname, job_status)

    @docopt_cmd
    def do_display_all_offices(self, args):
    	"""Usage: display_all_offices"""
    	display_offices(offices)

    @docopt_cmd
    def do_display_employee_office(self, args):
    	"""Usage: display_employee_office <fname> <lname>"""
    	first_name = args['<fname>']
    	last_name = args['<lname>']
    	display_persons_office(first_name, last_name)

    @docopt_cmd
    def do_display_full_offices(self, args):
    	"""Usage: display_full_offices"""
    	display_full_offices(full_offices)

    @docopt_cmd
    def do_display_full_living_spaces(self, args):
    	"""Usage: display_full_living_spaces"""
    	display_full_living_spaces(full_living_spaces)

    @docopt_cmd
    def do_print_room(self, args):
    	"""Usage print_room <room_name>"""
    	name = args['<room_name>']
    	display_room(name)
        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:

    MyInteractive().cmdloop()
print(opt)
