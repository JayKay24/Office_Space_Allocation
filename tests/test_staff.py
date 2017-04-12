import unittest

class StaffTest(unittest.TestCase):
    def setUp(self):
        self.staff = Staff("James", "Kinyua", "Staff")

    def testStaffHasFirstName(self):
        self.assertEqual(self.staff.firstName, "James")

if __name__ == "__main__":
	unittest.main()