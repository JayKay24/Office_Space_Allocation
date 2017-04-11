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