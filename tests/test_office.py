import unittest

class OfficeTest(unittest.TestCase):
    def setUp(self):
        self.office = Office("Blue")

    def testOfficeHasMaxNum6(self):
        self.assertEqual(self.office.max_num, 6)

    def testOfficeHasAttributeName(self):
        self.assertEqual(self.office.name, "Blue")

class CreateOfficeTests(unittest.TestCase):
    def setUp(self):
        self.name = "Blue"

    def testCreateOffice(self):
        self.office = create_office(self.name)
        self.assertEqual(self.office.name, "Blue")


if __name__ == "__main__":
	unittest.main()