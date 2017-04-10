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

if __name__ == "__main__":
    unittest.main()
