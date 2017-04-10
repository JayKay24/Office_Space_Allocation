"""
This module imports all the necessary classes to implement the controller aspect
of the MVC framework.
"""
from dojo import Dojo
from fellow import Fellow
from living_space import LivingSpace
from office import Office
from person import Person
from room import Room
from staff import Staff

# Init.
people = []
def create_office(args):
    """
    Accepts argument name to create an Office object.
    """
    office = Office(args["<room_name>"])
    return office

def create_living_space(args):
    """
    Accepts argument name to create a LivingSpace object.
    """
    living_space = LivingSpace(args["<name>"])
    return living_space

def create_person(args):
    """
    Accepts arguments name, status to create a Person object.
    """
    if args["<FELLOW|STAFF>"] == "FELLOW":
        person = Fellow(args["<person_name>"], args["<FELLOW|STAFF>"])
        if args["[wants_accommodation]"] == "Y":
            person.opt_in = True
    elif args["<FELLOW|STAFF>"] == "STAFF":
        person = Staff(args["<person>"], args["<FELLOW|STAFF>"])
    return person

def add_person(person):
    """
    Accepts an object to append to the people list.
    """
    people.append(person)
    print("Person added successfully")
    print(people)
    return people
