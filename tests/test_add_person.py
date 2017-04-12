from controller import create_person 

import unittest
class AddPersonTests(unittest.TestCase):
    def setUp(self):
        person = create_person("James", "Kinyua", "Fellow")

    def testAddPersonReturnsList(self):
        people = add_person(person)
        self.assertEqual(isinstance(people, list), True)

if __name__ == "__main__":
	unittest.main()
