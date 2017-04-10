import unittest

import person
import fellow
import living_space
import staff
import dojo
import room
import office

class PersonTest(unittest.TestCase):
    def testPersonHasName(self):
        guy = person.Person("James", "Fellow")
        self.assertEqual(guy.name, "James")

if __name__ == "__main__":
    unittest.main()
