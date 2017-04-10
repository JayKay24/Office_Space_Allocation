import unittest

import person
import fellow
import living_space
import staff
import dojo
import room
import office

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.guy = person.Person("James", "Fellow")
        
    def testPersonHasName(self):
        self.assertEqual(self.guy.name, "James")

    def testPersonHasStatus(self):
        self.assertEqual(self.guy.status, "Fellow")

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = room.Room()

    def testRoomHasFilledAttribute(self):
        self.assertEqual(self.room.filled, False)

class LivingSpaceTest(unittest.TestCase):
    def setUp(self):
        self.living_space = living_space.LivingSpace()

    def testLivingSpaceHasMaxNum4(self):
        self.assertEqual(self.living_space.max_num, 4)

class OfficeTest(unittest.TestCase):
    def setUp(self):
        self.office = office.Office()

    def testOfficeHasMaxNum6(self):
        self.assertEqual(self.office.max_num, 6)

if __name__ == "__main__":
    unittest.main()
