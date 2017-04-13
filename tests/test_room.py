import unittest
import sys

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = Room("Orange")

    def testRoomHasFilledAttribute(self):
        self.assertEqual(self.room.filled, False)

    def testRoomHasNameAttribute(self):
        self.assertEqual(self.room.name, "Orange")

if __name__ == "__main__":
	unittest.main()