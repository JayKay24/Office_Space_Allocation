import unittest
import sys

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class CreatePersonTests(unittest.TestCase):
    def setUp(self):
        self.fname = "James"
        self.lname = "Kinyua"
        self.status = "Fellow"

    def testCreatePerson(self):
        self.person = create_person(self.fname, self.lname, self.status)
        self.assertEqual(self.status, "Fellow")

if __name__ == "__main__":
	unittest.main()
