"""
This module imports all the necessary classes to implement the controller aspect
of the MVC framework.
"""
import random

from dojo import Dojo
from fellow import Fellow
from living_space import LivingSpace
from office import Office
from person import Person
from room import Room
from staff import Staff
from model import offices, living_spaces, fellows, staffs

def create_office(name):
    """
    Accepts argument name to create an Office object.
    """
    office = Office(name)
    print("Office created successfully!")
    offices.append(office)

def create_living_space(name):
    """
    Accepts argument name to create a LivingSpace object.
    """
    living_space = LivingSpace(name)
    print(living_space.name)
    print("Living Space created successfully!")
    living_spaces.append(living_space)

def create_person(person_fname, person_lname, job_status):
    """
    Accepts arguments name, status to create a Person object.
    """
    random_office = random.choice(offices)
    if job_status.upper() == "FELLOW":
        person = Fellow(person_fname, person_lname, job_status)
        person.assign_office_space(random_office.name)
        fellows.append(person)

    elif job_status.upper() == "STAFF":
        person = Staff(person_fname, person_lname, job_status)
        person.assign_office_space(random_office.name)
        staffs.append(person)

    return person

def display_persons_office(fname, lname):
    """
    Accepts a person object and displays their office name.
    """
    persons = fellows + staffs
    for person in persons:
        if fname == person.firstName and lname == person.lastName:
            print("\t" + person.firstName, person.lastName, person.office_name)
        else:
            print("No matching name in the database.")

def display_offices(offices):
    """
    Accepts a list of offices objects and displays each office name.
    """
    print("\tOffice Names\n")
    print("\t{:*^30s}\n".format("*"))
    print("\tThese are the offices in the database:\n")
    for office in offices:
        print("\t{}".format(office.name))