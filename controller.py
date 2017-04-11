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
def create_office(name):
    """
    Accepts argument name to create an Office object.
    """
    office = Office(name)
    print("Office created successfully!")
    print(Office.name)
    return office

def create_living_space(name):
    """
    Accepts argument name to create a LivingSpace object.
    """
    living_space = LivingSpace(name)
    print(living_space.name)
    return living_space

def create_person(person_name, job_status):
    """
    Accepts arguments name, status to create a Person object.
    """
    if job_status == "FELLOW":
        person = Fellow(person_name, job_status)
    elif job_status == "STAFF":
        person = Staff(person_name, job_status)
    print("Person created successfully")
    print(person)
    return person

def add_person(person):
    """
    Accepts an object to append to the people list.
    """
    people.append(person)
    print("Person added successfully")
    print(people)
    return people
