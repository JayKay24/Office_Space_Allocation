import unittest

import person
import fellow
import living_space
import staff
import dojo
import room
import office

from controller import create_office
from controller import create_living_space
from controller import create_person
from controller import add_person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.guy = person.Person("James", "Kinyua", "Fellow")
        
    def testPersonHasName(self):
        self.assertEqual(self.guy.firstName, "James")

    def testPersonHasStatus(self):
        self.assertEqual(self.guy.status, "Fellow")

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = room.Room("Orange")

    def testRoomHasFilledAttribute(self):
        self.assertEqual(self.room.filled, False)

    def testRoomHasNameAttribute(self):
        self.assertEqual(self.room.name, "Orange")

class LivingSpaceTest(unittest.TestCase):
    def setUp(self):
        self.living_space = living_space.LivingSpace("Black")

    def testLivingSpaceHasMaxNum4(self):
        self.assertEqual(self.living_space.max_num, 4)

    def testLivingSpaceHasNameAttribute(self):
        self.assertEqual(self.living_space.name, "Black")

class OfficeTest(unittest.TestCase):
    def setUp(self):
        self.office = office.Office("Blue")

    def testOfficeHasMaxNum6(self):
        self.assertEqual(self.office.max_num, 6)

    def testOfficeHasAttributeName(self):
        self.assertEqual(self.office.name, "Blue")

class FellowTest(unittest.TestCase):
    def setUp(self):
        self.fellow = fellow.Fellow("James", "Kinyua", "Fellow")

    def testFellowHasOptIn(self):
        self.assertEqual(self.fellow.opt_in, False)

class StaffTest(unittest.TestCase):
    def setUp(self):
        self.staff = staff.Staff("James", "Kinyua", "Staff")

    def testStaffHasFirstName(self):
        self.assertEqual(self.staff.firstName, "James")

class CreateOfficeTests(unittest.TestCase):
    def setUp(self):
        self.name = "Blue"

    def testCreateOffice(self):
        self.office = create_office(self.name)
        self.assertEqual(self.office.name, "Blue")

class CreateLivingSpaceTests(unittest.TestCase):
    def setUp(self):
        self.name = "Red"

    def testCreateLivingSpace(self):
        self.living_space = create_living_space(self.name)
        self.assertEqual(self.living_space.name, "Red")

class CreatePersonTests(unittest.TestCase):
    def setUp(self):
        self.fname = "James"
        self.lname = "Kinyua"
        self.status = "Fellow"

    def testCreatePerson(self):
        self.person = create_person(self.fname, self.lname, self.status)
        self.assertEqual(self.status, "Fellow")

class AddPersonTests(unittest.TestCase):
    def setUp(self):
        person = create_person("James", "Kinyua", "Fellow")

    def testAddPersonReturnsList(self):
        people = add_person(person)
        self.assertEqual(isinstance(people, list), True)

if __name__ == "__main__":
    unittest.main()
