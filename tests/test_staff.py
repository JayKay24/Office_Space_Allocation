import unittest
import sys

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class StaffTest(unittest.TestCase):
    def setUp(self):
        self.staff = Staff("James", "Kinyua", "Staff")

    def testStaffHasFirstName(self):
        self.assertEqual(self.staff.firstName, "James")

if __name__ == "__main__":
	unittest.main()