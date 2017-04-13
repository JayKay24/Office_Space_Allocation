"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    view create_room <room_type> <room_name>...
    view add_person <fname> <lname> <person_job> [<accom>]
    view display_all_offices
    view display_greeting
    view print_room <room_name>
    view print_allocations [<filename>]
    view display_full_offices
    view display_employee_office <fname> <lname>
    view give_office <fname> <lname>
    view (-i | --interactive)
    view (-h | --help)
Options:
    --accom
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
from controller import display_allocations
from controller import display_prog_greeting
from controller import allocate_office_space, allocate_living_space
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
                # Create an office object by calling create_office in the controller module.
        		create_office(item)
        	elif room_type.upper() == "LIVING":
                # Create a living_space object by calling create_living_space in the controller module.
        		create_living_space(item)


    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <fname> <lname> <person_job> [<accom>]"""

        job_status = args['<person_job>']
        person_fname = args['<fname>']
        person_lname = args['<lname>']
        accom = args['<accom>']
        # Create a person object
        person = create_person(person_fname, person_lname, job_status, accom)

    @docopt_cmd
    def do_display_all_offices(self, args):
    	"""Usage: display_all_offices"""

        # Call display_offices from the controller module to display all offices.
    	display_offices(offices)

    @docopt_cmd
    def do_display_employee_office(self, args):
    	"""Usage: display_employee_office <fname> <lname>"""
    	first_name = args['<fname>']
    	last_name = args['<lname>']
        # Call display_persons from the controller module to display a persons office.
    	display_persons_office(first_name, last_name)

    @docopt_cmd
    def do_display_full_offices(self, args):
    	"""Usage: display_full_offices"""

        # Call display_full_offices from the controller module to display full office spaces.
    	display_full_offices(full_offices)

    @docopt_cmd
    def do_display_full_living_spaces(self, args):
    	"""Usage: display_full_living_spaces"""

        # Call display_full_living_spaces from the controller module to display full living spaces.
    	display_full_living_spaces(full_living_spaces)

    @docopt_cmd
    def do_print_room(self, args):
    	"""Usage: print_room <room_name>"""
    	name = args['<room_name>']

        # Call display_room from the controller module to display a persons room.
    	display_room(name)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<filename>]"""

        people = fellows + staffs
        if args['<filename>']:
            # Call display_allocations from the controller module to write space allocations
            display_allocations(people, args['<filename>'])
        else:
            # Call display_allocations from the controller module to print space allocations
            display_allocations(people)

    @docopt_cmd
    def do_display_greeting(self, args):
        """Usage: display_greeting"""

        # Call display_prog_greeting from the controller module to print the program greeting.
        display_prog_greeting()

    @docopt_cmd
    def do_give_office(self, args):
        """Usage: give_office <fname> <lname>"""

        fname = args['<fname>']
        lname = args['<lname>']
        people = fellows + staffs
        for person in people:
            if person.firstName == fname and person.lastName == lname:
                # Call allocate_office_space from the controller module to allocate an office space.
                allocate_office_space(person)
                break
        else:
            print(fname, lname, "is neither a Fellow nor a Staff member.")

        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:

    MyInteractive().cmdloop()
print(opt)
