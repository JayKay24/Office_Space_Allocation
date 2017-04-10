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
    office = Office(name)
    return office
def create_living_space(name):
    living_space = LivingSpace(name)
    return living_space

def create_person(name, status):
    person = Person(name, status)
    return person
