"""
This module imports all the necessary classes to implement the controller aspect
of the MVC framework.
"""
import random

from dojo import Dojo
from Room.room import Room
from Room.office import Office
from Person.person import Person
from Person.fellow import Fellow
from Room.living_space import LivingSpace
from Person.staff import Staff
from model import offices, living_spaces, fellows, staffs, full_offices, full_living_spaces

def create_office(name):
    """
    Accepts argument name to create an Office object.
    """
    office = Office(name)
    print("An office called", name, "has been successfully created!")
    offices.append(office)

def create_living_space(name):
    """
    Accepts argument name to create a LivingSpace object.
    """
    living_space = LivingSpace(name)
    print(living_space.name)
    print("Living Space created successfully!")
    living_spaces.append(living_space)
    return living_space

def create_person(person_fname, person_lname, job_status, accom=""):
    """
    Accepts arguments name, status to create a Person object.
    """
    if job_status.upper() == "FELLOW":
        person = Fellow(person_fname, person_lname, job_status)
        while True:
            random_office = random.choice(offices)
            if random_office.spaces_left > 0:
                person.assign_office_space(random_office.name)
                random_office.allocate_space()
                break
            else:
                index_rand_off = offices.index(random_office)
                office = offices.pop(index_rand_off)
                full_offices.append(office)
        if accom.upper() == "Y" and person is Fellow():
            while True:
                random_living_space = random.choice(living_spaces)
                if random_living_space.spaces_left > 0:
                    person.assign_living_space(random_living_space.name)
                    print(person.firstName+ " has been allocated the living space "+ person.living_space_name)
                    random_living_space.allocate_space()
                    break
                else:
                    index_rand_liv_space = living_spaces.index(random_living_space)
                    living_space = living_spaces.pop(index_rand_liv_space)
                    full_living_spaces.append(living_space)

        fellows.append(person)

    elif job_status.upper() == "STAFF":
        person = Staff(person_fname, person_lname, job_status)
        while True:
            random_office = random.choice(offices)
            if random_office.spaces_left > 0:
                person.assign_office_space(random_office.name)
                random_office.allocate_space()
                break
            else:
                index_rand_off = offices.index(random_offices)
                office = offices.pop(index_rand_off)
                full_offices.append(office)

        staffs.append(person)
    print(person.firstName, "has been successfully added.")
    print(person.firstName, "has been allocated the office", person.office_name)

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

def display_object_types(objects_list):
    """
    Accepts a list of objects_list objects and displays each object_list name.
    """
    for object_type in objects_list:
        print("\t{:*^30s}\n".format(object_type.name))

def display_offices(offices):
    """
    Accepts a list of offices objects and displays each office name.
    """
    print("\tOffice Names\n")
    display_object_types(offices)

def display_full_offices(full_offices):
    """
    Accepts a list of full_offices objects and displays each office name.
    """
    print("Full Offices")
    display_object_types(full_offices)

def display_full_living_spaces(full_living_spaces):
    """
    Accepts a list of full_living_spaces objects and displays each living_space_name.
    """
    print("\tFull Living Spaces")
    display_object_types(full_living_spaces)

def display_room(name):
    """
    Accepts a name argument and loops through objects to determine if attributes 
    match name.
    """
    print("\t" + name)
    people = staffs + fellows

    for person in people:
        if person.office_name == name:
            print("\t" + person.firstName, person.lastName)
        elif person.status.upper() == "FELLOW":
            if person.living_space_name == name:
                print("\t" + person.firstName, person.lastName)

def display_allocations(people, filename=""):
    """
    Accepts a list of people objects and prints their name and room attributes.
    """
    if filename:
        with open(filename, 'w') as file_obj:
            for person in people:
                if person.status.upper() == "FELLOW":
                    file_obj.write(person.firstName + " " + person.lastName + " " + person.living_space_name + "\n")
                file_obj.write(person.firstName + " " + person.lastName + " " + person.office_name + "\n")
    else:
        for person in people:
            if person.status.upper() == "FELLOW":
                print(person.firstName + " " + person.lastName + " " + person.living_space_name)
            print(person.firstName + " " + person.lastName + " " + person.office_name)
