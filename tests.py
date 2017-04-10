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
        self.guy = person.Person("James", "Fellow")
        
    def testPersonHasName(self):
        self.assertEqual(self.guy.name, "James")

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
        self.fellow = fellow.Fellow("James", "Fellow")

    def testFellowHasOptIn(self):
        self.assertEqual(self.fellow.opt_in, False)

class StaffTest(unittest.TestCase):
    def setUp(self):
        self.staff = staff.Staff("James", "Staff")

    def testStaffHasName(self):
        self.assertEqual(self.staff.name, "James")

class CreateOfficeTests(unittest.TestCase):
    def setUp(self):
        self.name = "Blue"

    def testCreateOffice(self):
        office = create_office(self.name)
        self.assertEqual(self.office.name, "Blue")

if __name__ == "__main__":
    unittest.main()
